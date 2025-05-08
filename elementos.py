#### Importar librerias necesarias ####


#### Definicion de variables globales ####
elementos = [
    {
        'simbolo': 'H',
        'nombre': 'Hidrogeno',
        'numero_atomico': 1,
        'masa_atomica': 1.008,
        'estado': 'Gas'
    },
    {
        'simbolo': 'He',
        'nombre': 'Helio',
        'numero_atomico': 2,
        'masa_atomica': 4.002602,
        'estado': 'Gas'
    },
    {
        'simbolo': 'Li',
        'nombre': 'Litio',
        'numero_atomico': 3,
        'masa_atomica': 6.94,
        'estado': 'Sólido'
    }
]

#### Definicion de funciones ####
def nuevo_elemento():
    elemento_nuevo = {}
    elemento_nuevo['simbolo'] = input('Ingrese el simbolo del elemento: ')
    elemento_nuevo['nombre'] = input('Ingrese el nombre del elemento: ')
    elemento_nuevo['numero_atomico'] = int(input('Ingrese el numero atomico del elemento: '))
    elemento_nuevo['masa_atomica'] = float(input('Ingrese la masa atomica del elemento: '))
    elemento_nuevo['estado'] = input('Ingrese el estado del elemento: ')
    return elemento_nuevo

def imprimir_elemento(elemento: dict):
    # H(Hidrogeno):
    #     Masa atomica: 1.008
    #     Estado: Gas
    #     Numero atomico: 1
    print(f"{elemento['simbolo']}({elemento['nombre']}):")
    print(f"\tMasa atomica: {elemento['masa_atomica']}")
    print(f"\tEstado: {elemento['estado']}")
    print(f"\tNumero atomico: {elemento['numero_atomico']}")
    print('')

def buscar_simbolo():
    simbolo = input('Ingrese el simbolo del elemento: ')
    for elemento in elementos:
        if elemento['simbolo'].lower() == simbolo.lower():
            imprimir_elemento(elemento)
            return
    print('Elemento no encontrado')

def buscar_nombre():
    nombre = input('Ingrese el nombre del elemento: ')
    for elemento in elementos:
        if elemento['nombre'].lower() == nombre.lower():
            imprimir_elemento(elemento)
            return
    print('Elemento no encontrado')

def menu_de_busqueda():
    mensaje = '''
=== BUSQUEDA DE ELEMENTOS QUIMICOS ===
1. Buscar por simbolo
2. Buscar por nombre
'''
    print(mensaje)
    opcion = int(input('Ingrese una opcion: '))

    if opcion == 1:
        buscar_simbolo()
    elif opcion == 2:
        buscar_nombre()
    else:
        print('Opcion no valida, intente nuevamente')



### Funcion principal ###

if __name__ == '__main__':

    mensaje = '''
=== SISTEMA DE REGISTRO DE ELEMENTOS QUIMICOS ===
1. Agregar elemento
2. Listar elementos disponibles
3. Visualizar informacion de un elemento
4. Salir
'''
    salir = True

    while salir:
        print(mensaje)

        opcion = int(input('Ingrese una opcion: '))

        if opcion == 1:
            elementos.append(nuevo_elemento())
        elif opcion == 2:
            for elemento in elementos:
                imprimir_elemento(elemento)
        elif opcion == 3:
            menu_de_busqueda()
        elif opcion == 4:
            print('Saliendo del sistema...')
            salir = False
        else:
            print('Opcion no valida, intente nuevamente')
        
        _ = input('Presione enter para continuar...')
