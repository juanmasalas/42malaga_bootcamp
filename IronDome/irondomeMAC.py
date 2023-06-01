import argparse, time, logging, os, psutil, magic, hashlib,threading, signal, sys, subprocess
from daemonize import Daemonize
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import numpy as np
import datetime

pid = "/Users/jcueto-r/Desktop/irondome.pid"

files = []
objects = []
counter_event = 0
oldpercent_DU = 50
counter_Cripto = 0
counter_flag = 0

class Archivo:
    def __init__(self, path, hash, entropy, filetype, creationdate, newhash=None, newentropy=None, newfiletype=None, newcreationdate=None):
        self.path = path
        self.hash = hash
        self.entropy = entropy
        self.filetype = filetype
        self.creationdate = creationdate
        self.newhash = newhash
        self.newentropy = newentropy
        self.newfiletype = newfiletype
        self.newcreationdate = newcreationdate

def crear_objetos_archivos(file):
    hash = calculate_hash(file)
    entropy = calculate_entropy(file)
    creation_date = get_modified_date(file)
    i = Archivo(file,hash,entropy[0],entropy[1],creation_date,None,None,None,None)
    objects.append(i)

def evitar_duplicados():
    path_walk(ruta_critica, extensiones)
    for file in files:
        obj_paths = [obj.path for obj in objects]
        try:
            if file not in obj_paths:
                crear_objetos_archivos(file)
        except FileNotFoundError:
            print("Archivo no encontrado")

def comprobar_objetos(object):
    for obj in object:
        global counter_flag, counter_Cripto
        try:
            new_hash = calculate_hash(obj.path)
            new_entropy = calculate_entropy(obj.path)
            new_creation_date = get_modified_date(obj.path)
        except FileNotFoundError:
            files.remove(obj.path)
            objects.remove(obj)
        try:
            obj.newhash = new_hash
            obj.newentropy = new_entropy[0]
            if obj.entropy == None or obj.newentropy == None:
                obj.entropy = 0
                obj.newentropy = 0
            obj.newfiletype = new_entropy[1]
            obj.newcreationdate = new_creation_date
        except TypeError:
            pass
        if not extensiones or os.path.splitext(obj.path)[1] in extensiones:
            if obj.hash != obj.newhash:
                logging.info(f'<Path: {obj.path}, el hash ha cambiado de {obj.hash} a {obj.newhash}>')
                obj.hash = obj.newhash
                counter_flag += 1
            if obj.entropy != obj.newentropy:
                logging.info(f'<Path: {obj.path}, la entropia ha cambiado de {obj.entropy} a {obj.newentropy}>')
                obj.entropy = obj.newentropy
                counter_flag += 1
            if obj.filetype != obj.newfiletype:
                logging.info(f'<Path: {obj.path}, el tipo de archivo ha cambiado de {obj.filetype} a {obj.newfiletype}>')
                obj.filetype = obj.newfiletype
                counter_flag += 1
            if obj.creationdate != obj.newcreationdate:
                logging.info(f'<Path: {obj.path}, la fecha de creacion ha cambiado de {obj.creationdate} a {obj.newcreationdate}>')
                obj.creationdate = obj.newcreationdate
                counter_flag += 1
            if counter_flag > 2:
                logging.warning(f"Posible actividad criptográfica")
                counter_Cripto += 1
                t0 = datetime.datetime.now()    
                crypto_activity(t0)
            counter_flag = 0

def crypto_activity(t0):
    t1 = datetime.datetime.now()
    td = t1 - t0
    global counter_flag, counter_Cripto
    if counter_Cripto >= 3 and td < datetime.timedelta(seconds=1):
        i = 0
        while i < 5:
            logging.critical(f"Se ha detectado el uso intensivo de actividad criptográfica")
            i += 1
        counter_Cripto = 0
    
def path_walk(ruta, extensiones):
    for dirpath, dirnames, filenames in os.walk(ruta):
        for filename in filenames:
            if len(extensiones) == 0:
                file_path = os.path.join(dirpath, filename)
                if file_path not in files:
                    files.append(file_path)
            elif len(extensiones) >= 1:
                file_path = os.path.join(dirpath, filename)
                for a in extensiones:
                    if filename.endswith(a):
                         if file_path not in files:
                            files.append(file_path)

def calculate_hash(file):
    hash_obj = hashlib.md5()
    try:
        with open(file, 'rb') as f:
            for bloque in iter(lambda: f.read(4096), b''):
                hash_obj.update(bloque)
    except (FileNotFoundError, PermissionError, OSError):
        print("No se puede obtener el hash")
    hash = hash_obj.hexdigest()
    return hash

def calculate_entropy(file_path):
    try:
        file_type = magic.from_file(file_path, mime=True)
        with open(file_path, 'rb') as file:
            content = file.read()
            byte_counts = np.bincount(np.frombuffer(content, dtype=np.uint8))
            probabilities = byte_counts / len(content)
            probabilities = np.where(np.isclose(probabilities, 0), 1e-10, probabilities)  # Reemplazar valores cercanos a cero
            entropy = -np.sum(probabilities * np.log2(probabilities))
        return  entropy, file_type
    except (IsADirectoryError, FileNotFoundError):
        pass

def get_modified_date(file):
    timestamp = os.stat(file).st_birthtime
    fecha_creacion = datetime.datetime.fromtimestamp(timestamp)
    return fecha_creacion

def monitorizar_ruta(ruta):
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, ruta, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def config_logger():
    # logging.basicConfig(filename='/Users/jcueto-r/Desktop/irondome-' + str(datetime.datetime.now()) + '.log', level=logging.DEBUG, format='%(process)d - %(asctime)s - %(levelname)s - %(message)s - %(name)s')
    logging.basicConfig(filename='/Users/jcueto-r/Desktop/irondome-' + str(datetime.datetime.now()) + '.log', level=logging.INFO, format='%(process)d - %(asctime)s - %(levelname)s - %(message)s - %(name)s')
    logging.basicConfig(filename='/Users/jcueto-r/Desktop/irondome-' + str(datetime.datetime.now()) + '.log', level=logging.WARNING, format='%(process)d - %(asctime)s - %(levelname)s - %(message)s - %(name)s')

def comprobacion_memoria():
    mem = psutil.Process().memory_info().rss
    pid = os.getpid()
    logging.info(f'Memoria en uso: {format(mem/1024/1024, ".2f")} MB')
    if mem > 100000000:
        logging.warning(f'Se ha excedido la memoria en uso permitida de 100 MB. Se procede a suspender el proceso.')
        # os.kill(pid, signal.SIGSTOP) # Suspendes proceso, recuperar con fg
        # os.kill(pid, 9)
        os.kill(pid, signal.SIGCONT) # Continuas despues de parar

def check_disk_usage(ruta):
    try:
        disk_usage = psutil.disk_usage(ruta)
        percent_DU = disk_usage.percent
        logging.info(f'El uso de disco está al: {percent_DU:.2f} %')
        if percent_DU - oldpercent_DU >= 20:
            logging.warning(f'Se detecta abusos en la lectura de disco')
        else:
            pass
    except FileNotFoundError:
        pass

def leer_registros_criptoapi():
    try:
        # Comando para leer los registros del sistema
        if sys.platform == "darwin":
            # macOS
            comando = "log show --predicate 'eventMessage CONTAINS \"CriptoAPI\"' --style syslog --info"
        if sys.platform.startswith("linux"):
            # Linux (Debian, Ubuntu, etc.)
            comando = "journalctl --no-pager -q -o cat --grep=\"CriptoAPI\""
        else:
            print("El sistema operativo no es compatible.")
            return []
        # Ejecutar el comando y capturar la salida
        salida = subprocess.check_output(comando, shell=True, universal_newlines=True)
        # Procesar la salida de los registros y buscar eventos relacionados con la CriptoAPI
        eventos_criptoapi = buscar_eventos_criptoapi(salida)
        # Retornar los eventos encontrados
        logging.warning(f'Se han encontrado los siguientes registros del uso de alguna CriptoApi {eventos_criptoapi}')
        return eventos_criptoapi
    except subprocess.CalledProcessError:
        print("Error al leer los registros del sistema.")
        return []
    
def buscar_eventos_criptoapi(registros):
    # Implementa aquí la lógica para buscar eventos relacionados con la CriptoAPI en los registros
    # Puedes utilizar expresiones regulares, cadenas de búsqueda, o cualquier otro método que se adapte a tus necesidades y al formato de los registros
    eventos = []
    # Ejemplo: buscar eventos que contengan la cadena "CriptoAPI"
    for registro in registros.splitlines():
        if "CriptoAPI" in registro:
            eventos.append(registro)
    return eventos


class MyHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.processed_events = set()
        path_walk(ruta_critica, extensiones)
        for file in files:
            crear_objetos_archivos(file)
        # logging.info((f"__________________________ Evento número: {counter_event} ______________________"))
        # comprobacion_memoria()
        # check_disk_usage(ruta_critica)


    def on_created(self, event):
        if not extensiones or os.path.splitext(event.src_path)[1] in extensiones:
            global counter_event
            # if event in self.processed_events:
            #     return
            # self.processed_events.add(event)
            # self.path = event.src_path
            counter_event += 1
            logging.info((f"__________________________ Evento número: {counter_event} ______________________"))
            comprobacion_memoria()
            check_disk_usage(ruta_critica)
            logging.info(f'Se ha creado el archivo: {event.src_path} ')
            evitar_duplicados()
            matching_objects = [obj for obj in objects if obj.path == event.src_path]
            comprobar_objetos(matching_objects)
            leer_registros_criptoapi()
            print(len(files))
            print(len(objects))
            print("CREADO")

            return super().on_created(event) 
    
    def on_moved(self, event):
        if not extensiones or os.path.splitext(event.src_path)[1] in extensiones:
            global counter_event
            # if event in self.processed_events:
            #     return
            # self.processed_events.add(event)
            # self.path = event.src_path
            counter_event += 1
            logging.info((f"__________________________ Evento número: {counter_event} ______________________"))
            comprobacion_memoria()
            check_disk_usage(ruta_critica)
            evitar_duplicados()
            logging.info(f'Se ha movido/renombrado el archivo: {event.src_path} al archivo {event.dest_path} ')
            matching_objects = [obj for obj in objects if obj.path == event.src_path]
            comprobar_objetos(matching_objects)
            leer_registros_criptoapi()
            print(len(files))
            print(len(objects))
            print("MOVIDO/RENOMBRADO")
        
            return super().on_moved(event)
    
    def on_deleted(self, event):
        if not extensiones or os.path.splitext(event.src_path)[1] in extensiones:
            global counter_event
            # if event in self.processed_events:
            #     return
            # self.processed_events.add(event)
            # self.path = event.src_path    
            counter_event += 1
            logging.info((f"__________________________ Evento número: {counter_event} ______________________"))
            comprobacion_memoria()
            check_disk_usage(ruta_critica)
            logging.info(f'Se ha eliminado el archivo: {event.src_path} ')
            matching_objects = [obj for obj in objects if obj.path == event.src_path]
            comprobar_objetos(matching_objects)
            leer_registros_criptoapi()
            print(len(files))
            print(len(objects))
            print("ELIMINADO")

            return super().on_deleted(event)
    
    def on_modified(self, event):
        if not extensiones or os.path.splitext(event.src_path)[1] in extensiones:
            global counter_event
            # if event in self.processed_events:
            #     return
            # self.processed_events.add(event)
            # self.path = event.src_path
            counter_event += 1
            if event.is_directory == False:
                logging.info((f"__________________________ Evento número: {counter_event} ______________________"))
                comprobacion_memoria()
                check_disk_usage(ruta_critica)
                logging.info(f'Se ha modificado el archivo: {event.src_path}')
            evitar_duplicados()
            matching_objects = [obj for obj in objects if obj.path == event.src_path]
            comprobar_objetos(matching_objects)
            leer_registros_criptoapi()
            print(len(files))
            print(len(objects))
            print("MODIFICADO")

            return super().on_modified(event)

def main():
    config_logger()
    h2 = threading.Thread(name="hilo_2", target=monitorizar_ruta, args=(ruta_critica,))
    h2.start()
        

if __name__ == "__main__":
    # if os.geteuid() != 0:
    #     print("Error: Irondome must be run as root.")
    #     sys.exit(1)
    parser = argparse.ArgumentParser(description='Programa irondome')
    parser.add_argument('-m', nargs='*', type=str)
    args = parser.parse_args()
    ruta_critica = args.m[0]
    extensiones = args.m[1:]
    # main()
    daemon = Daemonize(app="irondome_analyzer", pid=pid, action=main)
    daemon.start()
    
