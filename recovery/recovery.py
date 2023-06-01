import subprocess
import os
import datetime
import win32com.client
import win32evtlog
import getpass
import psutil
import argparse
from browser_history import get_history

def get_browsers_histories(log_file_path, fecha_limite):
    log_file = f"get_browsers__histories__{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}_{getpass.getuser()}.txt"
    log_file_path = os.path.join(os.getcwd(), log_file)
    write_to_log(log_file_path, ["Historial de navegacion:"])
    print("Historial de navegacion:")
    outputs = get_history()  
    fecha_limite = fecha_limite.replace(tzinfo=None)
    for out in outputs.histories:
        time = out[0]
        time = time.replace(tzinfo=None)
        if time > fecha_limite:
            with open(log_file_path, "a", encoding="utf-8") as log_file:
                log_file.write(str(out[0]) + "\n")
                log_file.write(out[1] + "\n")
                log_file.write('-' * 50 + "\n")

def write_to_log(log_file_path, texts):
    with open(log_file_path, "a", encoding="utf-8") as log_file:
        for text in texts:
            log_file.write(text + "\n")


def write_to_log_events(events, log_file_path):
    try:
        with open(log_file_path, "a", encoding="utf-8") as log_file:
            for event in events:
                log_file.write("Evento:\n")
                for key, value in event.items():
                    log_file.write(f"{key}: {value}\n")
                log_file.write("\n")
    except Exception as e:
        print(f"Error al escribir en el archivo de log: {str(e)}")


def get_target_path(lnk_file):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(lnk_file)
    return shortcut.Targetpath


def get_recent_file_changes(log_file_path, fecha_limite):
    log_file = f"get_recent_file_changes_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}_{getpass.getuser()}.txt"
    log_file_path = os.path.join(os.getcwd(), log_file)
    write_to_log(log_file_path, ["Archivos recientes:"])
    print("Archivos recientes:")
    try:
        recent_files = []
        recent_folder = os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Recent")
        files = os.listdir(recent_folder)
        for file in files:
            file_path = os.path.join(recent_folder, file)
            if os.path.isfile(file_path):
                modified_time = os.path.getmtime(file_path)
                modified_datetime = datetime.datetime.fromtimestamp(modified_time)
                if modified_datetime >= fecha_limite:
                    if file.lower().endswith(".lnk"):
                        target_path = get_target_path(file_path)
                        if target_path:
                            recent_files.append(target_path)
                    else:
                        recent_files.append(file_path)
        if recent_files:
            write_to_log(log_file_path, recent_files)
            for file in recent_files:
                print(file)
        else:
            write_to_log(log_file_path, ["No se encontraron archivos recientes."])
            print("No se encontraron archivos recientes.")
    except Exception as e:
        print(f"Ocurrió un error al obtener los archivos recientes: {str(e)}")


def get_installed_programs(log_file_path, fecha_limite):
    log_file = f"get_installed_programs_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}_{getpass.getuser()}.txt"
    log_file_path = os.path.join(os.getcwd(), log_file)
    programs_found = []
    write_to_log(log_file_path, ["Programas instalados:"])
    print("Programas instalados:")
    try:
        wmi = win32com.client.GetObject("winmgmts:")
        programs = wmi.ExecQuery("SELECT Name, InstallDate FROM Win32_Product")
        for program in programs:
            name = program.Name
            install_date_str = program.InstallDate
            if install_date_str is not None:
                install_date = datetime.datetime.strptime(install_date_str, "%Y%m%d")
                if install_date >= fecha_limite:
                    write_to_log(log_file_path, [name])
                    programs_found.append(name)
                    print(name)
        if len(programs_found) == 0:
            write_to_log(log_file_path, ["No se encontraron programas."])
            print("No se encontraron programas.")
    except Exception as e:
        print(f"Error al obtener los programas instalados: {str(e)}")


def get_running_processes(log_file_path, fecha_limite):
    log_file = f"get_running_processes_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}_{getpass.getuser()}.txt"
    log_file_path = os.path.join(os.getcwd(), log_file)
    write_to_log(log_file_path, ["Procesos ejecutados:"])
    print("Procesos ejecutados:")
    for proc in psutil.process_iter(['pid', 'name', 'create_time']):
        try:
            # Obtener información del proceso
            pid = proc.info['pid']
            name = proc.info['name']
            create_time = datetime.datetime.fromtimestamp(proc.info['create_time'])
            # Verificar si el proceso se ejecutó dentro del rango de tiempo
            if create_time >= fecha_limite:
                process_info = f"PID: {pid}, Nombre: {name}, Tiempo de creación: {create_time}"
                write_to_log(log_file_path, [process_info])
                print(process_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Manejar excepciones de procesos que no se pueden acceder o ya no existen
            continue
    if not any(psutil.process_iter()):
        write_to_log(log_file_path, ["No se encontraron procesos ejecutados."])
        print("No se encontraron procesos ejecutados.")


def get_connected_devices(log_file_path):
    log_file = f"get_connected_devices_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}_{getpass.getuser()}.txt"
    log_file_path = os.path.join(os.getcwd(), log_file)
    write_to_log(log_file_path, ["Dispositivos conectados:"])
    print("Dispositivos conectados:")
    try:
        devices = set()  # Utilizar un conjunto para evitar dispositivos repetidos
        # Obtener los dispositivos conectados usando el comando 'wmic'
        result = subprocess.run(["wmic", "path", "win32_pnpentity", "get", "caption"], capture_output=True,
                                text=True)
        output_lines = result.stdout.strip().split('\n')
        for line in output_lines[1:]:
            device = line.strip()
            if device:
                devices.add(device)  # Agregar el dispositivo al conjunto
        # Escribir los resultados en el archivo de log y en la consola
        if devices:
            write_to_log(log_file_path, devices)
            for device in devices:
                print(device)
        else:
            write_to_log(log_file_path, ["No se encontraron dispositivos conectados."])
            print("No se encontraron dispositivos conectados.")
    except Exception as e:
        print(f"Error al obtener los dispositivos conectados: {str(e)}")


def get_connected_hard_drives(log_file_path, fecha_limite):
    log_file = f"get_connected_hard_drives_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}_{getpass.getuser()}.txt"
    log_file_path = os.path.join(os.getcwd(), log_file)
    write_to_log(log_file_path, ["Dispositivos de almacenamiento conectados:"])
    print("Dispositivos de almacenamiento conectados:")
    try:
        # Obtener la lista de discos duros conectados utilizando el comando wmic
        output = subprocess.check_output(["wmic", "logicaldisk", "get", "name"], encoding="utf-8")
        # Analizar la salida para obtener los nombres de los discos duros
        lines = output.strip().split("\n")
        hard_drives = [line.strip() for line in lines[1:] if line.strip()]
        # Escribir los resultados en el archivo de log y en la consola
        if hard_drives:
            write_to_log(log_file_path, hard_drives)
            for hard_drive in hard_drives:
                print(hard_drive)
        else:
            write_to_log(log_file_path, ["No se encontraron dispositivos de almacenamiento conectados."])
            print("No se encontraron dispositivos de almacenamiento conectados.")
    except Exception as e:
        print(f"Error al obtener los dispositivos de almacenamientos conectados: {str(e)}")


def get_event_logs(nombre_log, log_file_path, fecha_limite):
    log_file = f"get_event_logs_{nombre_log}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}_{getpass.getuser()}.txt"
    log_file_path = os.path.join(os.getcwd(), log_file)
    write_to_log(log_file_path, ["Eventos de log:"])
    print("Eventos de log:")
    fecha_limite = fecha_limite.timestamp()
    try:
        eventos = []
        hand = win32evtlog.OpenEventLog(None, nombre_log)
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
        eventos_totales = win32evtlog.GetNumberOfEventLogRecords(hand)

        for _ in range(eventos_totales):
            eventos_temp = win32evtlog.ReadEventLog(hand, flags, 0)
            if eventos_temp is None:
                break
            for evento in eventos_temp:
                if evento.StringInserts is not None:
                    evento_info = {
                        'ID': evento.EventID,
                        'Fecha y hora': evento.TimeGenerated.Format(),
                        'Origen': evento.SourceName,
                        'Categoría': evento.EventCategory,
                        'Usuario': evento.StringInserts[0] if len(evento.StringInserts) > 0 else '',
                        'Mensaje': evento.StringInserts[1] if len(evento.StringInserts) > 1 else '',
                        'Datos brutos': evento.StringInserts[2:] if len(evento.StringInserts) > 2 else ''
                    }
                    fecha_evento = evento.TimeGenerated.timestamp()
                    print(fecha_evento)
                    print(fecha_limite)
                    
                    if fecha_evento > fecha_limite:
                        print(int(fecha_evento))
                        print(int(fecha_limite))
                        eventos.append(evento_info)

        win32evtlog.CloseEventLog(hand)
        return eventos, log_file_path

    except Exception as e:
        print(f"Error al obtener los eventos de log: {str(e)}")



def main():
    # Configurar los argumentos de línea de comandos
    parser = argparse.ArgumentParser(description="Script para obtener información del sistema.")
    parser.add_argument("-d", "--days", type=int, help="Cantidad de días hacia atrás a considerar", default=7)
    args = parser.parse_args()

    # Calcular la fecha límite
    now = datetime.datetime.now()
    fecha_limite = now - datetime.timedelta(days=args.days)

    # Ruta del archivo de log
    log_file_path = os.path.join(os.getcwd(), "system_info_log.txt")

    # Obtener la información del sistema
    get_recent_file_changes(log_file_path, fecha_limite)
    get_installed_programs(log_file_path, fecha_limite)
    get_running_processes(log_file_path, fecha_limite)
    get_connected_devices(log_file_path)
    get_connected_hard_drives(log_file_path, fecha_limite)
    get_browsers_histories(log_file_path, fecha_limite)

    # Obtener los eventos de log de seguridad
    eventos_seguridad, log_file_path = get_event_logs("Security", log_file_path, fecha_limite)
    write_to_log_events(eventos_seguridad, log_file_path)

    # # Obtener los eventos de log de aplicaciones
    eventos_aplicaciones, log_file_path = get_event_logs("Application", log_file_path, fecha_limite)
    write_to_log_events(eventos_aplicaciones, log_file_path)

    # # Obtener los eventos de log del sistema
    eventos_sistema, log_file_path = get_event_logs("System", log_file_path, fecha_limite)
    write_to_log_events(eventos_sistema, log_file_path)


if __name__ == "__main__":
    main()