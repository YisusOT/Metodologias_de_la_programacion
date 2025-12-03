"""
Jesus Ignacio Olvera Trejo

Grupo IM 1-2

Matricula: 2530266
"""
# Problema 1: Sum of range with for
print('\n\n\n Problema 1\n')
"""
Descripción:
Calcula la suma de todos los enteros desde 1 hasta n (incluyendo n). 
Además, calcula la suma solo de los números pares en ese mismo rango usando un bucle for.
"""
suma = 0
even = 0
try:
  num = int(input('Set your final numbers to sum'))
  for number in range(0, num+1):
    suma = suma + number
  for number in range(0, num+1, 2):
    even = even + number
except:
  print('Set real number')
print(f'The sum is {suma}')
print(f'The sum of even is {even}')

"""
Entradas:
  num

Salidas
  suma_normal
  suma_even

Validaciones:
- Verificar que n pueda convertirse a int.
- n >= 1; si no se cumple, mostrar "Error: invalid input".
  
Casos:
  Set your final numbers to sum 5
  The sum is 15
  The sum of even is 6

  Set your final numbers to sum a
  Set real number
  The sum is 0
  The sum of even is 0

  Set your final numbers to sum -4
  The sum is 0
  The sum of even is 0
"""
# Problema 2:
print('\n\n\nProblema 2: \n')
"""
Descripción:
Genera y muestra la tabla de multiplicar de un número base, desde 1 hasta un límite m. 
"""
try:
  base = int(input('Set the base of the multiplication: '))
  limit = int(input("Set the limit of the multiplications: "))
  for number in range(1, limit+1):
    multiplication = base * number
    print(f'{base} x {number} = {multiplication}')
except:
  print('set a real number')
"""
Entradas:
  base
  limit

Salidas:
  multiplication

Validaciones:
- base y m convertibles a int.
- m >= 1; si no, "Error: invalid input".

Casos:
  Set the base of the multiplication: 7
  Set the limit of the multiplications: 4
  7 x 1 = 7
  7 x 2 = 14
  7 x 3 = 21
  7 x 4 = 28

  Set the base of the multiplication: a
  set a real number

  Set the base of the multiplication: -4
  Set the limit of the multiplications: 7
  -4 x 1 = -4
  -4 x 2 = -8
  -4 x 3 = -12
  -4 x 4 = -16
  -4 x 5 = -20
  -4 x 6 = -24
  -4 x 7 = -28
"""
# Problema 3:
print('\n\n\n Problema 3: \n')
"""
Descripción:
Lee números uno por uno hasta que el usuario ingrese un valor sentinela (por ejemplo, -1). 
Calcula el promedio de los números válidos ingresados y la cantidad de números leídos. 
Si el usuario sólo ingresa el sentinela sin números válidos, muestra un mensaje de error.
"""
try: 
    centinela = 0
    suma = 0
    count = 0
    while centinela <= -1:
        centinela = float(input('Set a number to sum: '))
        if centinela != -1:
            suma = suma + centinela
            count = count + 1
    if count == 0:
        print("Error, you don't set any number before the centinel")
    else:
        print(f'The sum of the numbers is {suma}')
        average = suma / count
        print(f'The average is {average}')
except:
    print('error in problem')

"""
Entradas:
  centinela

Salidas:
  suma
  average

Validaciones:
- Cada lectura debe intentar convertirse a float.
- Ignorar el sentinela en los cálculos.

Casos:
  Set a number to sum: 7
  Set a number to sum: 8
  Set a number to sum: 9
  Set a number to sum: 1
  Set a number to sum: 3
  Set a number to sum: 0
  Set a number to sum: -1
  The sum of the numbers is 28
  The average is 4.666666666666667

  Set a number to sum: 2
  Set a number to sum: 2
  Set a number to sum: 2
  Set a number to sum: 2
  Set a number to sum: -1
  The sum of the numbers is 8
  The average is 2.0

  Set a number to sum: a
  error in problem 
"""

# Problema 4:
print('\n\n\n Problema 4: \n')  
"""
Descripción:
Implementa un sistema sencillo de intento de contraseña. 
Define en el código una contraseña correcta (por ejemplo, "admin123"). 
El usuario tiene un máximo de MAX_ATTEMPTS intentos para introducirla. 
Si acierta dentro del límite, mostrar un mensaje de éxito. 
Si agota los intentos, mostrar un mensaje de bloqueo.
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

"""
Entradas:
  password

salidas:
  attmeps
  boolean:
    True = "lo lograste'
    False = 'Intenta otra vez'

Validaciones:
- MAX_ATTEMPTS > 0 (definido como constante en el código, por ejemplo 3).
- Contar correctamente los intentos.

Casos:
  Set your password: 4
  Set 4 digits
  you have 2 attemps more
  Set your password: 3456
  intenta otra vez
  you have 1 attemps more
  Set your password: -4afs
  Set a real PIN
  you have 0 attemps more
  acces denied

  Set your password: 1234
  acceso permitido

  Set your password: lsas
  Set a real PIN
  you have 2 attemps more
  Set your password: 3412
  intenta otra vez
  you have 1 attemps more
  Set your password: 1234
  acceso permitido
"""
# Problema 5:
print('\n\n\n Problema 5: \n')  
"""
Descripción:
Implementa un menú de texto que se repite hasta que el usuario seleccione la opción de salir. 
El programa debe ejecutar la acción correspondiente a cada opción y volver a mostrar el menú hasta que se elija 0.
"""
import time
import random
option = 's'

while option != '0':
  time.sleep(0)
  print('\n Set 1 to show a poem')
  print('Set 2 to show a random number')
  print('Set 3 to print the numbers in range(1, 10000000000)')
  print('Set 0 to exit')
  option = input('-  ')
  if option == '1':
    time.sleep(1)
    print('hola')
    time.sleep(1)
    print('camote')
    time.sleep(1)
    print('FIN')
    time.sleep(5)
  elif option == '2':
    rand = random.randint(0, 10000)
    print(rand)
  elif option == '3':
    time.sleep(4)
    print('1')
    time.sleep(3)
    print('the numbers in range(1, 10000000000)')
    print('FIN')
    time.sleep(1)
"""
Entradas:
  option

salidas:
  random_number
  poem
  numbers

Validaciones:
- Normalizar option (por ejemplo, convertir a int con manejo de error).
- Asegurar que sólo 0,1,2,3 sean aceptadas como válidas.

Casos:
  Set 1 to show a poem
  Set 2 to show a random number
  Set 3 to print the numbers in range(1, 10000000000)
  Set 0 to exit
  -  3
  1
  the numbers in range(1, 10000000000)
  FIN

  Set 1 to show a poem
  Set 2 to show a random number
  Set 3 to print the numbers in range(1, 10000000000)
  Set 0 to exit
  -  2
  8916

  Set 1 to show a poem
  Set 2 to show a random number
  Set 3 to print the numbers in range(1, 10000000000)
  Set 0 to exit
  -  1
  hola
  camote
  FIN
"""

# Problema 6
print('\n\n\n Problema 6: \n')
"""
Descripción:
Usa bucles for anidados para imprimir un patrón de asteriscos en forma de triángulo rectángulo. Por ejemplo, para n = 4:
Además, imprime un segundo patrón invertido (opcional si lo deseas extender, pero documenta tu decisión).
"""
try:
  quantity = int(input('Set the quantity of lines: '))
  list_of_numbers = list(value for value in range(1, quantity+1))
  for number in list_of_numbers:
    print('*' * number)
  list_of_numbers.sort(reverse=True)
  for number in list_of_numbers:
    print('*' * number)
except:
  print('Set a real number')

"""
Entradas:
  quantity

Salidas:
  triangule
  triangule_reverse

Validaciones:
- n convertible a int.
- n >= 1; si no, "Error: invalid input".

Casos:
  Set the quantity of lines: 7
  *
  **
  ***
  ****
  *****
  ******
  *******
  *******
  ******
  *****
  ****
  ***
  **
  *

  Set the quantity of lines: -3

  Set the quantity of lines: a
  Set a real number
"""
"""
Conclusion:
  Para conlcuir, por la realizacion de este trabajo aprendi mucho de como generar
  bucles, tanto finitos como infinitos, cosa muy util para poder crear codigos mas
  completos y que pueda permanecer abierto hasta que el usuario decida cuando acaba 
  y no tenga que volver a ejecutar el codigo cada vez

Referencias:
https://www.srcodigofuente.es/curso-php/bucle-while-ejemplos
https://hektorprofe.github.io/python/funcionalidades-avanzadas/funciones-generadoras
https://developers.google.com/edu/python/lists?hl=es-419
https://www.freecodecamp.org/espanol/news/como-asignar-funciones-a-listas-en-python-3-0
https://docs.python.org/es/3.13/howto/functional.html
Google IA
"""