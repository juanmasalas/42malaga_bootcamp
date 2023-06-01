import psutil
import subprocess
import time

def verificar_proceso(nombre_proceso):
    for proceso in psutil.process_iter(['name']):
        if proceso.info['name'] == nombre_proceso:
            return True
    return False

def iniciar_script(script_path):
    subprocess.Popen(['python', script_path])

# Nombre del proceso que deseas verificar
nombre_proceso = 'nombre_del_proceso.py'

# Ruta al script que deseas iniciar si el proceso no está en ejecución
ruta_script = 'ruta_al_script.py'

# Contador y tiempo inicial
contador = 0
tiempo_inicial = time.time()

while True:
    if verificar_proceso(nombre_proceso):
        print("El proceso está en ejecución.")
    else:
        print("El proceso no está en ejecución. Iniciando el script...")
        iniciar_script(ruta_script)
        contador += 1
    
    # Verificar si se supera el límite de 10 veces en 1 minuto
    tiempo_actual = time.time()
    tiempo_transcurrido = tiempo_actual - tiempo_inicial
    if contador > 10 and tiempo_transcurrido < 60:
        print("Se ha superado el límite de 10 veces en menos de 1 minuto. Deteniendo el script de control.")
        break
    
    # Reiniciar el contador si ha pasado más de 1 minuto
    if tiempo_transcurrido >= 60:
        contador = 0
        tiempo_inicial = tiempo_actual
    
    # Esperar un tiempo antes de verificar nuevamente
    time.sleep(5)  # Puedes ajustar este valor al intervalo de verificación deseado
