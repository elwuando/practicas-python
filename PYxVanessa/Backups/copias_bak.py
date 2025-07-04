import os
import shutil
import psutil
import logging
from datetime import datetime


# Rutas de origen y destino de los backups
origen = 'D:/OneDrive - CONFECCIONES BRAVASS S.A.S/Documentos/practicas-python/PYxVanessa/Backups/origen'
destino = 'D:/OneDrive - CONFECCIONES BRAVASS S.A.S/Documentos/practicas-python/PYxVanessa/Backups/destino'

# Configuracion basica del logging, crea archivos log por fecha actual YYYY-MM-DD.log
logging.basicConfig(filename=f"logs/{datetime.now().strftime('%Y-%m-%d')}.log", level=logging.DEBUG, format='%(message)s')


# Registra eventos como diccionario formateado en el log
def registrar_log(tipo, evento, ruta):

    log = {
        'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'tipo': tipo.upper(),
        'evento': evento,
        'ruta': ruta
    }

    # Formatear manualmente como texto tipo dict
    mensaje = str(log)

    logging.error(mensaje)


# Verifica que las dos carpetas existan y tengan permisos de lectura y/o escritura
def validar_carpetas(origen, destino):
    # verifica el la carperta este ne el origen
    if not os.path.isdir(origen):
        registrar_log('ERROR', 'La ruta no es un directorio', origen)
        return False

    # Verifica que la carpeta origen se pueda leer
    if not os.access(origen, os.R_OK):
        registrar_log('ERROR', 'Sin permisos de lectura', origen)
        return False

    # verifica que la carpeta destino existe
    if not os.path.isdir(destino):
        registrar_log('ERROR', 'La carpeta de destino no es un directorio', destino)
        return False

    # Verifica si se puede escribir en la carpeta destino
    if not os.access(destino, os.W_OK):
        registrar_log('ERROR', 'Sin permisos de escritura en destino', destino)
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
    registrar_log('INFO', f'Se encontraron {len(archivos)} archivos .BAK', origen)

    if not archivos:
        registrar_log('INFO', 'No se encontraron archivos .BAK', origen)
        return False

    return archivos


# Calcula el magnitud total de los archivos en bytes
def calcular_magnitud_total(origen, archivos):
    total = 0
    for archivo in archivos:
        try:
            ruta = os.path.join(origen, archivo)
            total += os.path.getsize(ruta)
            registrar_log('INFO', f'Magnitud total de archivos .BAK: {total} bytes', origen)
        except (FileNotFoundError, PermissionError, OSError):
            continue
    return total


# Verifica si hay espacio suficiente en la carpeta destino
def validar_espacio_disponible(destino, magnitud_requerido):
    espacio_libre = psutil.disk_usage(destino).free

    if espacio_libre >= magnitud_requerido:
        registrar_log('INFO', f'Espacio suficiente en destino', destino)
        return True
    else:
        registrar_log('WARNING', f'Espacio insuficiente en destino', destino)
        return False


# Elimina archivos .bak antiguos hasta liberar el espacio necesario
def liberar_espacio(destino, espacio_necesario):
    archivos = [os.path.join(destino, nombre) for nombre in os.listdir(destino) if nombre.endswith('.bak')]
    archivos.sort(key=os.path.getmtime)  # Ordena por fecha de modificación (más antiguos primero)
    acumulado = 0

    for archivo in archivos:
        acumulado += os.path.getsize(archivo)  # Suma magnitud del archivo
        os.remove(archivo)  # Elimina archivo

        if acumulado >= espacio_necesario:
            registrar_log('INFO', f'Se liberaron {acumulado} bytes', destino)
            break  # Detiene si se ha liberado lo necesario
    return acumulado  # Retorna espacio total liberado


# Valida un archivo: existencia, magnitud > 0 y lo mueve al destino si es válido
def validar_archivo(origen, destino):
    if not os.path.isfile(origen):  # Verifica si el archivo existe
        return False
    if os.path.getsize(origen) == 0:  # Verifica si el archivo está vacío
        return False
    try:
        nombre = os.path.basename(origen)  # Obtiene el nombre del archivo
        destino_final = os.path.join(destino, nombre)
        shutil.move(origen, destino_final)  # Mueve el archivo
        registrar_log('INFO', 'Archivo movido con exito', destino_final)
        return True
    except:
        registrar_log('ERROR', 'Error al mover el archivo', origen)
        return False


if __name__ == '__main__':

    # Si las rutas no son válidas o no tienen permisos
    if not validar_carpetas(origen, destino):
        exit()

    # Si la lista está vacía o hubo error finaliza
    archivos = listar_archivos(origen)
    if not archivos:
        exit()

    # Calcula el magnitud total de todos los archivos .bak listados
    magnitud_total = calcular_magnitud_total(origen, archivos)

    # Verifica si hay suficiente espacio libre en destino para mover los archivos
    if not validar_espacio_disponible(destino, magnitud_total):
        liberar_espacio(destino, magnitud_total)
        if not validar_espacio_disponible(destino, magnitud_total):
            registrar_log('ERROR', 'No se pudo liberar espacio suficiente', destino)
            exit()

    for archivo in archivos:
        ruta_origen = os.path.join(origen, archivo)
        if validar_archivo(ruta_origen, destino):
            registrar_log('INFO', 'El archivo se traslado correctamente', ruta_origen)
        else:
            registrar_log('ERROR', 'Error al trasladar el archivo, Archivo vacio', ruta_origen)
