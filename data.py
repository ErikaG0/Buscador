from pprint import pprint
from faker import Faker
import random
import json
from datetime import datetime

def generador_data_info():
    # Instancia del objeto 
    fakke = Faker('es_ES')

    palabras_clave = ["violencia", "estafa", "alimentos", "salud", "pension", "medicinas"]
    
    # Genera una lista de diccionarios
    data_falsa = []
    
    for _ in range(5):    
        # Generar datos ficticios para una Tutela
        Tutela = {
            "id": random.randint(1000, 9999),
            "titulo": fakke.sentence(),
            "resumen": f"{fakke.paragraph()} {random.choice(palabras_clave)}",
            "fecha": fakke.date_this_year(),
        }
        data_falsa.append(Tutela)
    return data_falsa

#llamada a la funcion 
resultado_funcion = generador_data_info()


def guardar_datos_en_archivo(datos, nombre_archivo):
    for dict_tutela in datos:
        dict_tutela['fecha'] = dict_tutela['fecha'].strftime('%Y-%m-%d')
    with open(nombre_archivo,'w') as archivo:
        json.dump(datos, archivo, indent=4)

# Suponiendo que tienes los datos generados en una variable llamada 'datos_generados'
guardar_datos_en_archivo(resultado_funcion, 'archivo.json')