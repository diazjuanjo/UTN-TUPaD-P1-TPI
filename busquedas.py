import validaciones
import filtros

def buscar_pais(lista_paises):
    if not lista_paises:
        print("No hay países en la lista para buscar")
        return
    
    termino_a_buscar = validaciones.validar_cadena_no_vacia("Ingrese nombre o parte del país a buscar: ")

    resultados = []

    for pais in lista_paises:
        if termino_a_buscar.lower() in pais['nombre'].lower():
            resultados.append(pais)

    if resultados:
        print(f"\nPaíses encontrados que incluyen '{termino_a_buscar}': ")
        filtros.mostrar_lista_paises(resultados)
    else:
        print(f"No se encontraron países que coincidan con '{termino_a_buscar}'")