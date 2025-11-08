def validar_entero_positivo(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.isdigit() and int(entrada) > 0:
            return int(entrada)
        else:
            print("Error: Debe ingresar un número entero positivo")

def validar_cadena_no_vacia(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.strip():
            return entrada
        else:
            print("Error: El campo no puede estar vacío")