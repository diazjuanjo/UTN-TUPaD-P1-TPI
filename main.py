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
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                print("\n== 1. Agregar un país ==")
            case "2":
                print("\n== 2. Actualizar datos de un país ==")
            case "3":
                print("\n== 3. Buscar un país por nombre ==")
            case "4":
                print("\n== 4. Filtrar países ==")
            case "5":
                print("\n== 5. Ordenar países ==")
            case "6":
                print("\n== 6. Mostrar estadísticas==")
            case "7":
                print("\n== 7. Salir (y guardar datos) ==")
                break
            case _:
                print("Error: Ingrese un número de 1-7")

main()