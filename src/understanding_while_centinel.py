
"""
un programa que sume numeros hasta que el usuario escriba la palabra salir,
el programa tambien debe decir: 
    - cuentos numeros ingreso el usuraio
    - cual fue el minimo
    - cual fue el maximo
"""
counter = 0
lista = []
centinel = 'c'
while centinel != 'salir':
    try:
        num1 = float(input('Set your first number: '))
        num2 = float(input('Set the second number: '))
        suma = num1 + num2
        print(suma)
        lista.append(suma)
        counter = counter + 1
        centinel = input('to exit set "salir" ')
    except:
        print('Error in something')

lista_ordenada = sorted(lista, reverse=False)

print(f'the small sum is {lista_ordenada[0]}')
print(f'the big sum is {lista_ordenada[-1]}')
print(f'You make {counter} sums')
print(f'your sums are {lista}')



print('\n\n\n')


centinel = 'c'
lista = []
counter = 0
suma = 0
while centinel != 'salir':
    try:
        num = (input('Set your number: (set "salir" to exit) '))
        if num.isdigit():
            num1 = float(num)
            lista.append(num1)
            counter = counter + 1
        else:
            centinel = num
    except:
        print('error in something')
if lista == []:
    print('no hiciste nunguna suma')
else:
    lista_ordenada = sorted(lista, reverse=False)
    print(f'the small sum is {lista_ordenada[0]}')
    print(f'the big sum is {lista_ordenada[-1]}')
    print(f'You make {counter} numbers')
    print(f'your numbers are {lista}')
    for value in lista_ordenada:
        suma = suma + value

    print(f'Your final sum is {suma}')