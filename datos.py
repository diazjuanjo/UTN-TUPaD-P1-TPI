import csv
import os

def cargar_datos(ruta_archivo):
    lista_paises = []

    if not os.path.exists(ruta_archivo):
        print(f"El archivo '{ruta_archivo}' no se encontró.")
        return []
    
    with open(ruta_archivo, mode='r', encoding='utf-8', newline='') as archivo:
        lector_csv = csv.DictReader(archivo)

        for fila in lector_csv:
            lista_paises.append({
                "nombre": fila["nombre"],
                "poblacion": int(fila["poblacion"]),
                "superficie": int(fila["superficie"]),
                "continente": fila["continente"],
            })
    return lista_paises

def guardar_datos(lista_paises, ruta_archivo):
    if not lista_paises:
        print("No hay datos para guardar")
        return
    
    with open(ruta_archivo, mode='w', encoding='utf-8', newline='') as archivo:
        escritor_csv = csv.DictWriter(archivo, fieldnames=['nombre', 'poblacion', 'superficie', 'continente'])
        escritor_csv.writeheader()
        escritor_csv.writerows(lista_paises)