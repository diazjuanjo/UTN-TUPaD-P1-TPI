import filtros

def obtener_nombre(pais):
    return pais['nombre']

def obtener_poblacion(pais):
    return pais['poblacion']

def obtener_superficie(pais):
    return pais['superficie']

def ordenar_paises(lista_paises):
    if not lista_paises:
        print("No hay países para ordenar")
        return
    
    print("Seleccione el criterio de ordenamiento:")
    print("1. Por Nombre")
    print("2. Por Población")
    print("3. Pro Superficie")
    opcion = input("Opción: ")

    orden_ascendente = input("¿Orden ascendente (S/N)? ").strip().upper()
    es_decendente = (orden_ascendente != 'S')

    lista_ordenada = []

    match opcion:
        case "1":
            lista_ordenada = sorted(lista_paises, key=obtener_nombre, reverse=es_decendente)

        case "2":
            lista_ordenada = sorted(lista_paises, key=obtener_poblacion, reverse=es_decendente)

        case "3":
            lista_ordenada = sorted(lista_paises, key=obtener_superficie, reverse=es_decendente)

        case _:
            print("Opción no válida")

    print("\n--- Lista de Países Ordenada ---")
    if not lista_ordenada:
        print("No se pudo ordenar la lista")
    else:
        filtros.mostrar_lista_paises(lista_ordenada)