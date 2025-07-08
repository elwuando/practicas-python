import os
import shutil
import psutil
import logging
from datetime import datetime


# Rutas de origen y destino de los backups
origen = 'D:/OneDrive - CONFECCIONES BRAVASS S.A.S/Documentos/practicas-python/PYxVanessa/Backups/origen'
destino = 'D:/OneDrive - CONFECCIONES BRAVASS S.A.S/Documentos/practicas-python/PYxVanessa/Backups/destino'


# Registra eventos como diccionario formateado en el log
def registrar_log(tipo, evento, ruta):

    carpeta_logs = 'logs'
    # Si no existe la carpeta la crea
    if not os.path.exists(carpeta_logs):
        os.makedirs(carpeta_logs)

    # Verifica si el sistema de logging ya tiene configurado un manejador (handler); si no, lo configura
    if not logging.getLogger().hasHandlers():
        # Configuracion basica del logging, crea archivos log por fecha actual YYYY-MM-DD.log
        logging.basicConfig(
            filename=f"logs/{datetime.now().strftime('%Y-%m-%d')}.log",
            level=logging.DEBUG,
            format='%(message)s',
            filemode='a'  # no sobrescribir el archivo existente
        )

    # Construir el diccionario del evento
    log = {
        'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'tipo': tipo.upper(),
        'evento': evento,
        'ruta': ruta
    }

    # Convertir el diccionario a texto plano
    mensaje = str(log)

    # Si el tipo no existe, por defecto usa logging.info
    # Obtener la función del nivel de log (info, error, etc.) y registrar el mensaje
    getattr(logging, tipo.lower(), logging.info)(mensaje)


# Verifica que las dos carpetas existan y tengan permisos de lectura y/o escritura
def validar_carpetas(origen, destino):
    # verifica que la ruta origen exista y sea un directorio
    if not os.path.isdir(origen):
        registrar_log('ERROR', 'El Origen no es un directorio(Carpeta)', origen)
        return False

    # Verifica que la carpeta origen posea permisos de escritura
    if not os.access(origen, os.W_OK):
        registrar_log('ERROR', 'Sin permisos de escritura en Origen', origen)
        return False

    # verifica que la ruta destino exista y sea un directorio
    if not os.path.isdir(destino):
        registrar_log('ERROR', 'El Destino no es un directorio(Carpeta)', destino)
        return False

    # Verifica que la carpeta destino posea permisos de escritura
    if not os.access(destino, os.W_OK):
        registrar_log('ERROR', 'Sin permisos de escritura en Destino', destino)
        return False

    registrar_log('INFO', 'Carpetas validas y accesibles', f'{origen} -> {destino}')
    return True


# Lista de archivos .bak de la carpeta origen
def listar_archivos(origen):
    archivos = []

    # Realizamos el recorrido por todas los archivos de la carpeta
    for archivo in os.listdir(origen):
        if archivo.lower().endswith('.bak') and os.path.isfile(os.path.join(origen, archivo)):
            archivos.append(archivo)

    if not archivos:
        registrar_log('INFO', 'No se encontraron archivos .BAK', origen)
        return []
    # se registra cuantos fueron encontrados
    registrar_log('INFO', f'Se encontraron {len(archivos)} archivos .BAK', origen)

    return archivos


# Calcula el magnitud total de los archivos en bytes
def calcular_magnitud_total(origen, archivos):
    total = 0

    for archivo in archivos:
        ruta = os.path.join(origen, archivo)
        total += os.path.getsize(ruta)
    registrar_log('INFO', f'Magnitud total de los archivos .BAK: {total} bytes', origen)
    return total


# Verifica si hay espacio suficiente en la carpeta destino
def validar_espacio_disponible(destino, magnitud_requerida):
    espacio_libre = psutil.disk_usage(destino).free  # Obtiene el espacio libre disponible en la unidad donde esta la carpeta destino

    if espacio_libre >= magnitud_requerida:
        registrar_log('INFO', f'Espacio suficiente en Destino', destino)
        return True
    else:
        registrar_log('WARNING', f'Espacio insuficiente en Destino', destino)
        return False


# Elimina archivos .bak antiguos hasta liberar el espacio necesario
def liberar_espacio(destino, espacio_necesario):
    archivos = [os.path.join(destino, nombre) for nombre in os.listdir(destino) if nombre.endswith('.bak')]  # Comprencion de listas
    archivos.sort(key=os.path.getmtime)  # Ordena por fecha de modificacion (mas antiguos primero)

    # Fecha y hora actual
    ahora = datetime.now()

    # contadores de espacio liberado y cantidad de archivos eliminados
    acumulado = 0
    eliminados = 0

    # Recorre todos los archivos .bak menos el mas reciente que seria el ultimo de la lista
    for archivo in archivos:
        fecha_modificacion = datetime.fromtimestamp(os.path.getmtime(archivo))
        dias_antiguedad = (ahora - fecha_modificacion).days
        if dias_antiguedad < 30 or fecha_modificacion.date() == ahora.date():
            continue

        try:
            acumulado += os.path.getsize(archivo)
            os.remove(archivo)
            eliminados += 1
        except Exception as e:
            registrar_log('ERROR', f'No se pudo eliminar el archivo: {e}', archivo)
            continue

        if acumulado >= espacio_necesario:
            registrar_log('INFO', f'Se liberaron {acumulado} bytes eliminando {eliminados} archivo(s)', destino)
            return

    # Si no fue suficiente
    registrar_log('ERROR', f'No se libero el espacio suficiente. Solo se liberaron {acumulado} bytes', destino)


# validamos que un archivo exista y no este vacío
def validar_archivo(origen):
    if not os.path.isfile(origen):  # Verifica que el archivo exista
        registrar_log('ERROR', 'El archivo no existe', origen)
        return False

    if os.path.getsize(origen) == 0:  # Verifica que no este vacio
        registrar_log('ERROR', 'El archivo se encuentra vacio', origen)
        return False

    registrar_log('INFO', 'El archivo es valido', origen)
    return True


# Verifica si un archivo está bloqueado o en uso por otro proceso
def archivo_bloqueado(ruta):
    try:
        # Intenta abrir el archivo en modo lectura binaria
        with open(ruta, 'rb'):
            return False  # El archivo no está bloqueado
    except (OSError, PermissionError):
        # Si ocurre un error al abrir el archivo es que esta bloqueado
        return True  # El archivo está bloqueado o en uso


# Traslada un archivo desde la carpeta origen hasta la carpeta destino
def trasladar_archivo(origen, destino):
    try:
        nombre = os.path.basename(origen)  # Extrae nombre del archivo
        destino_final = os.path.join(destino, nombre)  # Construye ruta destino
        shutil.move(origen, destino_final)  # Mueve el archivo
        registrar_log('INFO', 'El archivo se traslado con exito', destino_final)
        return True
    except Exception:
        registrar_log('ERROR', 'Error al trasladar el archivo', origen)
        return False


def generar_backup():
    if not validar_carpetas(origen, destino):
        return

    archivos = listar_archivos(origen)
    if not archivos:
        return

    magnitud_total = calcular_magnitud_total(origen, archivos)

    if not validar_espacio_disponible(destino, magnitud_total):
        liberar_espacio(destino, magnitud_total)
        if not validar_espacio_disponible(destino, magnitud_total):
            return

    for archivo in archivos:
        ruta_origen = os.path.join(origen, archivo)
        if archivo_bloqueado(ruta_origen):
            registrar_log('WARNING', 'Archivo bloqueado. No se puede procesar en este momento.', ruta_origen)
            continue
        if validar_archivo(ruta_origen):
            trasladar_archivo(ruta_origen, destino)
        else:
            registrar_log('ERROR', 'Archivo invalido o vacio', ruta_origen)


if __name__ == '__main__':
    generar_backup()
