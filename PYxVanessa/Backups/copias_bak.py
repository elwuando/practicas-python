import os
import shutil
import psutil
import logging
from datetime import datetime


# Definir cada funcion por proceso
origen = 'D:\OneDrive - CONFECCIONES BRAVASS S.A.S\Documentos\practicas-python\PYxVanessa\Backups\origen'
destino = 'D:\OneDrive - CONFECCIONES BRAVASS S.A.S\Documentos\practicas-python\PYxVanessa\Backups\destino'
logging.basicConfig(filename=f"logs/{datetime.now().strftime('%Y-%m-%d')}.log", level=logging.DEBUG, format='%(message)s')



def validar_carpetas(origen, destino):
    if not os.path.isdir(origen):
        registrar_log('ERROR', 'La ruta no es un directorio', origen)
        return False

    if not os.access(origen, os.R_OK):
        registrar_log('ERROR', 'Sin permisos de lectura', origen)
        return False

    if not os.path.isdir(destino):
        registrar_log('ERROR', 'La carpeta de destino no es un directorio', destino)
        return False

    if not os.access(destino, os.W_OK):
        registrar_log('ERROR', 'Sin permisos de escritura en destino', destino)
        return False

    registrar_log('INFO', 'Carpetas válidas y accesibles', f'{origen} -> {destino}')
    return True



def listar_archivos(origen):
    archivos = []

    for archivo in os.listdir(origen):
        if archivo.lower().endswith('.bak') and os.listdir(os.path.join(origen, archivo)):
            archivos.append(archivo)

    if not archivos:
        registrar_log('INFO', 'No se encontraron archivos .BAK', origen)
        return False

    return archivos



def calcular_tamaño_total(origen, archivos):
    total = 0
    for archivo in archivos:
        try:
            ruta = os.path.join(origen, archivo)
            total += os.path.getsize(ruta)
        except (FileNotFoundError, PermissionError, OSError):
            continue
    return total



def validar_espacio_disponible(destino, tamano_requerido):
    espacio_libre = psutil.disk_usage(destino).free

    if espacio_libre >= tamano_requerido:
        registrar_log('INFO', 'Espacio suficiente en destino', destino, espacio_libre)
        return True
    else:
        registrar_log('WARNING', 'Espacio insuficiente en destino', destino, espacio_libre)
        return False



def registrar_log(tipo, evento, ruta):
    # Construir dict como string
    log = {
        'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'tipo': tipo.upper(),
        'evento': evento,
        'ruta': ruta
    }

    # Formatear manualmente como texto tipo dict
    mensaje = str(log)

    logging.error(mensaje)



def liberar_espacio(destino, espacio_necesario):
    archivos = [os.path.join(destino, nombre) for nombre in os.listdir(destino) if nombre.endswith('.bak')]
    archivos.sort(key=os.path.getmtime)
    acumulado = 0
    for archivo in archivos:
        acumulado += os.path.getsize(archivo)
        os.remove(archivo)
        if acumulado >= espacio_necesario:
            break
    return acumulado



def validar_archivo(origen, destino):
    if not os.path.isfile(origen):
        return False
    if os.path.getsize(origen) == 0:
        return False
    try:
        nombre = os.path.basename(origen)
        destino_final = os.path.join(destino, nombre)
        shutil.move(origen, destino_final)
        return True
    except:
        return False
    
'''
Falta Organizar el tema de los loggings en las funciones, mas especificamente en los condicionales
'''

if __name__ == '__main__':
    pass
