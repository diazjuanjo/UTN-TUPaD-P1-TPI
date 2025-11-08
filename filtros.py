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
