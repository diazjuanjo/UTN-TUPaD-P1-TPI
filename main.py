import validaciones
import datos
import busquedas
import filtros
import ordenamiento
import estadisticas

def agregar_pais(lista_paises):
    print("Ingrese los datos del nuevo país: ")

    nombre = validaciones.validar_cadena_no_vacia("Nombre: ")
    poblacion = validaciones.validar_entero_positivo("Población: ")
    superficie = validaciones.validar_entero_positivo("Superficie (km2): ")
    continente = validaciones.validar_cadena_no_vacia("Continente: ")

    nuevo_pais = {
        'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente,
    }

    lista_paises.append(nuevo_pais)
    print(f"{nombre} fué agregado")

def actualizar_pais(lista_paises):
    if not lista_paises:
        print("No hay países en la lista para actualizar")
        return
    
    nombre_a_buscar = validaciones.validar_cadena_no_vacia("Ingrese el nombre del país que quiere actualizar: ")

    pais_encontrado = None

    for pais in lista_paises:
        if pais['nombre'].lower() == nombre_a_buscar.lower():
            pais_encontrado = pais
            break

    if pais_encontrado:
        print(f"País encontrado: {pais_encontrado['nombre']}")
        print(f"Población actual: {pais_encontrado['poblacion']}")
        print(f"Superficie actual: {pais_encontrado['superficie']} km2")

        nueva_poblacion = validaciones.validar_entero_positivo("Ingrese la nueva población: ")
        nueva_superficie = validaciones.validar_entero_positivo("Ingrese la nueva superficie (km2): ")

        pais_encontrado['poblacion'] = nueva_poblacion
        pais_encontrado['superficie'] = nueva_superficie

        print(f"Datos de '{pais_encontrado['nombre']}' actualizados")
    else:
        print(f"Error: No se encontró '{nombre_a_buscar}'")

def mostrar_menu():
    print("\n" + "=" * 40)
    print("--- GESTIÓN DE DATOS DE PAÍSES ---")
    print("=" * 40)
    print("1. Agregar un país")
    print("2. Actualizar datos de un país")
    print("3. Buscar un país por nombre")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Salir (y guardar datos)")
    print("=" * 40)


def main():
    lista_paises = datos.cargar_datos('paises.csv')

    if not lista_paises:
        print("No se pudieron cargar datos. Se iniciará con una lista vacía")
        lista_paises = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                print("\n== 1. Agregar un país ==")
                agregar_pais(lista_paises)
            case "2":
                print("\n== 2. Actualizar datos de un país ==")
                actualizar_pais(lista_paises)
            case "3":
                print("\n== 3. Buscar un país por nombre ==")
                busquedas.buscar_pais(lista_paises)
            case "4":
                print("\n== 4. Filtrar países ==")
                filtros.filtrar_paises(lista_paises)
            case "5":
                print("\n== 5. Ordenar países ==")
                ordenamiento.ordenar_paises(lista_paises)
            case "6":
                print("\n== 6. Mostrar estadísticas==")
                estadisticas.mostrar_estadisticas(lista_paises)
            case "7":
                print("\n== 7. Salir (y guardar datos) ==")
                datos.guardar_datos(lista_paises, 'paises.csv')
                print("Chau")
                break
            case _:
                print("Error: Ingrese un número de 1-7")

main()