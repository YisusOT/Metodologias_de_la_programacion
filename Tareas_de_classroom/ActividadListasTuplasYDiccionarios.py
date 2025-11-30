"""
Jesus Ignacio Olvera Trejo

Grupo IM 1-2

Matricula: 2530266

"""
# Problema 1
print('\nProblema 1\n')
"""
Descripción:
Trabaja con una lista de productos (strings) y sus cantidades (enteros). El programa debe:
1) Crear una lista inicial de productos.
2) Permitir agregar un nuevo producto al final.
3) Mostrar la cantidad total de elementos en la lista.
4) Verificar si un producto específico está en la lista (booleano is_in_list).
"""
import random
print('Hi')
products = ['camote', 'chamoy', 'papa', 'choripan']
price = [15, 18, 27, 20]
decision = 'c'
while True:
  decision = input('What product you want add? (set "finish" to end) ')
  if decision == 'finish':
    break
  elif decision in products:
    print('This product is in the list')   # Verifica si el producto esta en la lista
  else:
    products.append(decision)
    new_price = random.randint(1, 100)
    price.append(int(new_price))

suma = 0
for value in price:
  suma = suma + value

list_of_products = " ".join(products)
list_of_price = " ".join(str(price))
print(f'your list of products is {list_of_products}')
print(f'They price are {list_of_price}')
print(f'You have {len(products)} products in list')
print(f'Your total price is {suma}')

# Problema 2
print('\n\n\nProblema 2\n')
"""
Descripción:
Usa tuplas para representar dos puntos en un plano 2D: (x1, y1) y (x2, y2). El programa debe:
1) Crear dos tuplas point_a y point_b a partir de entradas numéricas.
2) Calcular la distancia euclidiana entre ambos puntos.
3) Crear una nueva tupla midpoint con el punto medio entre ellos.
"""
try:
  x1 = int(input('Set your X1 coordinate: '))
  y1 = int(input('Set your y1 coordinate: '))
  x2 = int(input('Set your x2 coordinate: '))
  y2 = int(input('Set your y2 coordinate: '))
  point_a = (x1, y1)
  point_b = (x2, y2)
  distance = ((point_b[1] - point_a[1])**2 + (point_b[0]-point_a[0])**2)**(1/2)
  mid_point = (((point_a[0] + point_b[0])/2), ((point_a[1] + point_b[1])/2) )
  print(f'your distance is {distance} ')
  print(f'the midpoint is {mid_point} ')
  print(f'the coordinates are {point_a} {point_b} ')
except:
  print('Error in something')

# Problema 3:
print('\n\n\nProblema 3\n')

""""
Descripción:
Administra un pequeño catálogo de productos usando un diccionario donde:
- clave: nombre del producto (string)
- valor: precio unitario (float)
El programa debe:
1) Crear un diccionario inicial con al menos 3 productos.
2) Leer el nombre de un producto y la cantidad a comprar.
3) Calcular el total a pagar si el producto existe.
4) Si el producto no existe, mostrar un mensaje de error.
"""
final_cost = 0.0
catalogo_mandarina = {
  'camote' : 15.99,
  'chamoy' : 17.50,
  'papa' : 27.99,
  'choripan' : 30.50,
}
catalogo_mandela = {}
products = ", ".join(catalogo_mandarina)
prices = catalogo_mandarina
print(f'We have this products: {products}')
print(f'The price of this products are: {prices}')
while True:
  sell_product = input('What are you buy? ("end" to exit) ')
  if sell_product.strip().lower() == 'end':
    break
  
  if sell_product in catalogo_mandarina:
    try:
      amount = int(input('How much do you want? '))
      catalogo_mandela[sell_product] = amount
    except:
      print('type error')
      break
  else:
    print('This product is NOT in sell')

print(catalogo_mandela)
for key, value in catalogo_mandela.items():
  if key in catalogo_mandarina:
    final_cost = final_cost + (value*(catalogo_mandarina[key]))

print(final_cost)

# Problema 4
print('\n\n\nProblema 4: \n')

"""
Descripción:
Administra las calificaciones de un grupo usando un diccionario:
- clave: nombre del estudiante (string)
- valor: lista de calificaciones (list of float)
El programa debe:
1) Crear un diccionario con al menos 3 estudiantes, cada uno con una lista de calificaciones.
2) Leer el nombre de un estudiante.
3) Calcular el promedio de sus calificaciones.
4) Indicar si el estudiante está aprobado (average >= 70.0) con un booleano is_passed.
"""
students = {
  'Edson' : [8.5, 9, 10],
  'Rodrigo' : [8, 7.5, 10],
  'Humberto' : [10, 9.5, 8.4],
}
suma = 0.0
student = " ".join(students)
print(f'The students are {student}')

who_student = input("Who student's calification You want? ")

if who_student.title() in students:
  student = students[who_student.title()]
  print(f'The studen {who_student} califications are: {student}')
  for value in student:
    suma = suma + value
  amount_digits = len(student)
  average = suma / amount_digits
  print(f'The average of this student is {average}')
else:
  print('This student is NOT in the list')

# Problema 5:
print('\n\n\n Problema 5 \n')

"""
Descripción:
Cuenta la frecuencia de cada palabra en una oración usando:
- Una lista de palabras.
- Un diccionario donde:
  - clave: palabra (string)
  - valor: frecuencia (int)
El programa debe:
1) Leer una oración.
2) Convertirla a minúsculas y separarla en una lista de palabras.
3) Construir un diccionario de frecuencias.
4) Mostrar el diccionario completo y la palabra más frecuente.
"""
setence = str(input('set your setence: '))
words = list(setence.split())
dictionary = {}
for value in words:
  if value in dictionary:
    dictionary[value] = dictionary[value] + 1
  else:
    dictionary[value] = 1
print(dictionary)

# Problema 6:
print('\n\n\n Problema 6 \n')
"""
Descripción:
Implementa un mini "contact book" usando un diccionario donde:
- clave: nombre de contacto (string)
- valor: número de teléfono (string)
El programa debe:
1) Crear un diccionario inicial con algunos contactos.
2) Leer una acción action_text ("ADD", "SEARCH" o "DELETE").
3) Según la acción:
   - "ADD": lee name y phone, agrega o actualiza el contacto.
   - "SEARCH": lee name y muestra el teléfono si existe.
   - "DELETE": lee name y elimina el contacto si existe.
4) Mostrar un mensaje indicando el resultado de la operación.
"""
contact_book = {}
loop = 'c'
while loop.strip().lower() != 'yes':
  print('\nSet 1 to add or modify a contact')
  print('Set 2 to search a contact')
  print('Set 3 to remove a contact')
  print('Set 4 to show the list of contacts')
  option = str(input('What do you want? '))
  true_option = option.strip().lower()

  if true_option == '1' or true_option == 'add':
    try:
      contact = str(input('Name of contact: ')).strip().upper()
      number = str(input('number of contact '))
      contact_book[contact] = number
      print(f'You add a {contact} ({number}) to contact book')
    except:
      print('Error to add, try again')
  elif true_option == '2' or true_option == 'search':
    try:
      contact = str(input('Name of contact: ')).strip().upper()
      print(f'The number of {contact} is {contact_book[contact]}')
    except:
      print('Error to search, Try again')
  elif true_option == '3' or true_option == 'delete':
    try:
      contact = str(input('Name of contact: ')).strip().upper()
      del contact_book[contact]
    except:
      print('Error to delete, try again')
  elif true_option == '4' or true_option == 'show list' or true_option == 'list':
    try:
      for key, value in contact_book.items():
        print(f'{key} : {value}')
    except:
      print('Error to show the list, try again')
  else:
    print('Set a real option')

  loop = input('Do you finish? Yes/No ')