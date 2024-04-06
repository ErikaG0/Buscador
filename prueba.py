import json
from pprint import pprint

def cargar_datos_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        datos = json.load(archivo)
    return datos
#lista datos
datos = cargar_datos_desde_archivo('archivo.json')

def buscador(datos):
    pprint(datos)
    #diccionario vacio
    indices = {}
    filtro = ["violencia", "estafa", "alimentos", "salud", "pensión", "medicinas"]
    
    #recorre cada elemto de datos
    for i, dato in enumerate(datos):
        #contenido de resumen lo divide cada palabra y lo ingresa en una lista
        palabras = dato["resumen"].split()
        
        pprint(palabras)
        #recorre la lista de palabras
        for g in palabras:
            #si la palabra esta en el filto ingresa segundo if
            if g in filtro:
                #si la palabra esta en el indice
                if g in indices:
                    # se añade el inidce
                    indices[g].append(i)
                    
                else:
                    #se crea la entrada  y el inidce 
                    indices[g] = [i]
    return indices

pprint(buscador(datos))