"""
Jesus Ignacio Olvera Trejo

Grupo IM 1-2

Matricula: 2530266
"""
# Problema 1:
print('\n\n\n Problema 1\n')
"""
Descripción:
Calcula la suma de todos los enteros desde 1 hasta n (incluyendo n). 
Además, calcula la suma solo de los números pares en ese mismo rango usando un bucle for.
"""
suma = 0
even = 0
try:
  n = int(input('Set your final numbers to sum'))
  for number in range(0, n+1):
    suma = suma + number
  for number in range(0, n+1, 2):
    even = even + number
except:
  print('Set real number')
print(f'The sum is {suma}')
print(f'The sum of even is {even}')

# Problema 2:
print('\n\n\nProblema 2: \n')
"""
Descripción:
Genera y muestra la tabla de multiplicar de un número base, desde 1 hasta un límite m. 
"""
base = int(input('Set the base of the multiplication: '))
limit = int(input("Set the limit of the multiplications: "))
for number in range(1, limit+1):
  multiplication = base * number
  print(f'{base} x {number} = {multiplication}')

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
    while centinela != -1:
        centinela = int(input('Set a number'))
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
    print('error in problem 3')

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

# Problema 6
print('\n\n\n Problema 6: \n')
"""
Descripción:
Usa bucles for anidados para imprimir un patrón de asteriscos en forma de triángulo rectángulo. Por ejemplo, para n = 4:
Además, imprime un segundo patrón invertido (opcional si lo deseas extender, pero documenta tu decisión).
"""
quantity = int(input('Set the quantity of lines: '))
list_of_numbers = list(value for value in range(1, quantity+1))
for number in list_of_numbers:
  print('*' * number)
list_of_numbers.sort(reverse=True)
for number in list_of_numbers:
  print('*' * number)
