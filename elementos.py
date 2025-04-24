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
        print('Se agregara un elemento')
    elif opcion == 2:
        print('Se listaran los elementos disponibles')
    elif opcion == 3:
        print('Se visualizara la informacion de un elemento')
    elif opcion == 4:
        print('Saliendo del sistema...')
        salir = False
    else:
        print('Opcion no valida, intente nuevamente')
