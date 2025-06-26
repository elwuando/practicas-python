import os
import shutil
import psutil
import logging

# Definir cada funcion por proceso
origen = 'D:\OneDrive - CONFECCIONES BRAVASS S.A.S\Documentos\practicas-python\PYxVanessa\Backups\origen'
destino = 'D:\OneDrive - CONFECCIONES BRAVASS S.A.S\Documentos\practicas-python\PYxVanessa\Backups\destino'

def validar_carpeta(origen):
    if not os.path.exists(origen):
        logging.error(f'ERROR | Carpeta no existe | {origen}')
        return False

    if not os.access(origen, os.R_OK):
        logging.error(f'ERROR | Sin permisos de lectura | {origen}')
        return False
    
    else:
        logging.info(f'INFO | Carpeta válida y accesible | {origen}')
        return True

def listar_archivos(origen):
    archivos = []

    for archivo in os.listdir(origen):
        if archivo.lower().endswith('.bak') and os.path.isfile(os.path.join(origen, archivo)):
            archivos.append(archivo)

    if not archivos:
        registrar_log('info', 'No se encontraron archivos .BAK', '', origen)

    return archivos

def calcular_tamaño_total(origen, archivos):
    total = 0
    for archivo in archivos:
        ruta = os.path.join(origen, archivo)
        total += os.path.getsize(ruta)
    return total

def registrar_log():
    # Registrar cada evento según su acción.
    pass


def validar_espacio_disponible(destino, tamano_requerido):
    espacio_libre = psutil.disk_usage(destino).free

    if espacio_libre >= tamano_requerido:
        registrar_log('info', 'Espacio suficiente en destino', '', destino, espacio_libre)
        return True
    else:
        registrar_log('warning', 'Espacio insuficiente en destino', '', destino, espacio_libre)
        return False
    

def liberar_espacio():
    # Liberar espacio eliminando los backups más antiguos hasta contar con el espacio necesario para los nuevos backups 
    pass

def validar_archivo():
    # Que no este bloqueado
    # Que pese mas de 0 MB
    # Si el archivo es valido moverlo a la carpeta Destino
    pass
