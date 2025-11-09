import validaciones

def mostrar_lista_paises(lista_paises):
    if not lista_paises:
        print("No se encontraron coincidencias")
        return
    
    print("\n--- Resultados ---\n")
    print(f"{'Nombre':<25} | {'Continente':<15} | {'Población':>15} | {'Superficie (km2)':>20}")
    print("-" * 80)

    for pais in lista_paises:
        nombre = pais['nombre']
        continente = pais['continente']
        poblacion = pais['poblacion']
        superficie = pais['superficie']
        print(f"{nombre:<25} | {continente:<15} | {poblacion:>15,} | {superficie:>20,}")

def filtrar_paises(lista_paises):
    if not lista_paises:
        print("No hay países para filtrar")
        return
    
    print("\n--- Menú de Filtros ---")
    print("1. Filtrar por Continente")
    print("2. Filtrar por Rango de Población")
    print("3. Filtrar por Rango de Superficie")
    opcion = input("Seleccione una opción: ")

    resultados = []

    match opcion:
        case "1":
            continente_buscado = validaciones.validar_cadena_no_vacia("Ingrese el nombre del continente: ")
            for pais in lista_paises:
                if pais['continente'].lower() == continente_buscado.lower():
                    resultados.append(pais)
            print(f"\nPaíses en '{continente_buscado}':")
            mostrar_lista_paises(resultados)
         
        case "2":
            print("Ingrese el rango de población")
            poblacion_min = validaciones.validar_entero_positivo("Población mínima: ")
            poblacion_max = validaciones.validar_entero_positivo("Población máxima: ")

            if poblacion_min > poblacion_max:
                print("Error: La población mínima no puede ser mayor que la máxima")
                return
            
            for pais in lista_paises:
                if poblacion_min <= pais['poblacion'] <= poblacion_max:
                    resultados.append(pais)
            print(f"\nPaíses con población entre {poblacion_min:,} y {poblacion_max:,}:")
            mostrar_lista_paises(resultados)

        case "3":
            print("Ingrese el rango de superficie (en km2)")
            superficie_min = validaciones.validar_entero_positivo("Superficie mínima: ")
            superficie_max = validaciones.validar_entero_positivo("Superficie máxima: ")

            if superficie_min > superficie_max:
                print("Error: La superficie mínima no puede ser mayor que la máxima")
                return
            
            for pais in lista_paises:
                if superficie_min <= pais['superficie'] <= superficie_max:
                    resultados.append(pais)
            print(f"\nPaíses con superficie entre {superficie_min:,} y {superficie_max:,}:")
            mostrar_lista_paises(resultados)

        case _:
            print("Opción no válida")