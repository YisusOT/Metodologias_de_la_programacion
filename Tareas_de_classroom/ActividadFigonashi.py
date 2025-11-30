"""
Jesus Ignacio Olvera Trejo

Grupo IM 1-2

Matricula: 2530266

Trabajo: Serie de Fibonacci
    La serie de Fibonacci es una secuencia infinita de números donde cada término es la suma de los dos anteriores, 
    comenzando usualmente con 0 y 1 (o 1 y 1). La secuencia se genera sumando los dos números previos: 
        0,1,1(0+1),2(1+1),3(1+2),5(2+3),8(3+5),
     y así sucesivamente.

    Para este trabajo, el usuario dara un numero que representa la posicion del numero en la serie, por ello debemos usar
    un algoritmo que pueda usar n numeros para n terminos, en otras palabras, que se pueda escoger cualquier numero natural
    entero hasta infinito y que aun asi el algoritmo arroje un resultado
"""
# verdadero codigo:
try:
  x = 0
  numbers = [0, 1]
  posicion = int(input('what posicion do you want?'))
  for coor in range(1, posicion-1):
    n = numbers[-1] + numbers[-2]
    numbers.append(n)
  for number in numbers:
    x = x + 1
    print(f'{x}.- {number}')
except:
  print('Set real numbers')


# Problema de serie de fibonacci:
""" Este es el primer codigo, el cual está mal
try:
    aurea = (1 + (5**(1/2)))/2
    n = int(input("Set the number of terms of the Fibonacci's serie: "))
    if n >= 0:
        serie = [value for value in range(0, (n+1))]
        for x in serie:
            fibonacci = (aurea**x - ((-aurea)**(-x)))/(5**(1/2))
            print(f"{x}.- {round(fibonacci)}")
    else:
        print("set a natural number")
except:
    print("Set a real number")
"""  # Posicion 71, a partir de ahi el redondeo se va para arriba (en la posicion 71 se pasa con 1)
