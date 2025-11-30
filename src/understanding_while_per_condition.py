"""
Vamos a realizar un programa que defina un pin como contraseña
Despues vamos a darle 3 intentos para adivinarlo
si el usuario adivina el pin, mostrar acceso permitido
si se equivoca, el programa debe de dar cuantos intentos le quedan y si se acaban, decir acceso denegado
"""
attemps = 3
PIN = 1234
while attemps != 0:
    try:
        password = int(input('Set your password: '))
        if len(str(password)) == 4:
            if password == PIN:
                print('acceso permitido')
                break
            else:
                print('intenta otra vez')
                attemps = attemps -1
        else:
            print('Set 4 digits')
            attemps = attemps - 1
    except:
        print('Set a real PIN')
        attemps = attemps - 1   
    print(f'you have {attemps} attemps more')
    if attemps == 0:
        print('acces denied')

