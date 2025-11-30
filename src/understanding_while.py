"""
Usamos el while para ejecuatr un bloque de codigo mientras una condicion sea verdadera
"""

# Ejemplo

# Verificar si un numero esta en un rango de 10 y 20
while True: # While infinito
    try:
        num = int(input('Set your number in 10 and 20  '))

        if num > 10 and num <20:
            print('is in range')
            break
        else:
            print('out of range')
    except ValueError:
        print('set a real number')
    except KeyboardInterrupt:
        print('\n end of program by user')
        break