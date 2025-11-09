def mostrar_estadisticas(lista_paises):
    if not lista_paises:
        print("No hay paises para calcular estadísticas")
        return
    
    pais_mas_poblacion = lista_paises[0]
    pais_menos_poblacion = lista_paises[0]

    suma_poblacion_total = 0
    suma_superficie_total = 0
    cantidad_paises = len(lista_paises)

    conteo_continentes = {}

    for pais in lista_paises:
        poblacion_actual = pais['poblacion']

        if poblacion_actual > pais_mas_poblacion['poblacion']:
            pais_mas_poblacion = pais

        if poblacion_actual < pais_menos_poblacion['poblacion']:
            pais_menos_poblacion = pais

        suma_poblacion_total = suma_poblacion_total + poblacion_actual
        suma_superficie_total = suma_superficie_total + pais['superficie']

        continente = pais['continente']
        if continente in conteo_continentes:
            conteo_continentes[continente] = conteo_continentes[continente] + 1
        else:
            conteo_continentes[continente] = 1

    print("\n--- ESTADÍSTICAS GLOBALES ---")
    print(f"País con mayor población: {pais_mas_poblacion['nombre']} ({pais_mas_poblacion['poblacion']} habitantes)")
    print(f"País con menor población: {pais_menos_poblacion['nombre']} ({pais_menos_poblacion['poblacion']} habitantes)")

    if cantidad_paises > 0:
        promedio_poblacion = suma_poblacion_total / cantidad_paises
        promedio_superficie = suma_superficie_total / cantidad_paises
        print(f"Población promedio: {promedio_poblacion:.2f} habitantes")
        print(f"Superficie promedio: {promedio_superficie:.2f} km2")

    print("\n--- Países por Continente ---")
    if not conteo_continentes:
        print("No hay datos de continentes")
    else:
        for continente in conteo_continentes:
            cantidad = conteo_continentes[continente]
            print(f"- {continente}: {cantidad} país(es)")
