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
  decision = input('What product you want add? (set "finish" to end) ').lower().strip()
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

"""
Entradas:
  desicion

Salidas:
  list_of_products
  list_of_price
  quantity_products
  suma

Validaciones:
- initial_items_text no vacío tras strip().
- Separar la cadena por comas y eliminar espacios extra en cada elemento.
- new_item y search_item no vacíos.
- Manejar el caso de lista inicial vacía si el estudiante lo decide (documentar decisión).

Casos:
  What product you want add? (set "finish" to end) CAMOTE
  This product is in the list
  What product you want add? (set "finish" to end) cloro
  What product you want add? (set "finish" to end) finish
  your list of products is camote chamoy papa choripan cloro
  They price are [ 1 5 ,   1 8 ,   2 7 ,   2 0 ,   7 4 ]
  You have 5 products in list
  Your total price is 154

  What product you want add? (set "finish" to end) 6
  What product you want add? (set "finish" to end) d
  What product you want add? (set "finish" to end) 3
  What product you want add? (set "finish" to end) finish
  your list of products is camote chamoy papa choripan 6 d 3
  They price are [ 1 5 ,   1 8 ,   2 7 ,   2 0 ,   5 3 ,   5 7 ,   4 4 ]
  You have 7 products in list
  Your total price is 234

  Hi
  What product you want add? (set "finish" to end) finish
  your list of products is camote chamoy papa choripan
  They price are [ 1 5 ,   1 8 ,   2 7 ,   2 0 ]
  You have 4 products in list
  Your total price is 80
"""

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

"""
Entradas:
  x1
  y1
  x2
  y2

Salidas:
  distance
  mid_point
  coordinates

Validaciones:
- Verificar que las 4 entradas se puedan convertir a float.
- No se requieren restricciones adicionales en el rango.

Casos:
  Set your X1 coordinate: 1
  Set your y1 coordinate: 2
  Set your x2 coordinate: 3
  Set your y2 coordinate: 4
  your distance is 2.8284271247461903
  the midpoint is (2.0, 3.0)
  the coordinates are (1, 2) (3, 4)

  Set your y1 coordinate: 6
  Set your x2 coordinate: -5
  Set your y2 coordinate: 9
  your distance is 3.0
  the midpoint is (-5.0, 7.5)
  the coordinates are (-5, 6) (-5, 9)

  Set your X1 coordinate: 7
  Set your y1 coordinate: a
  Error in something
"""
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
  sell_product = input('What are you buy? ("end" to exit) ').lower().strip()
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

"""
Entradas:
  sell_product
  amount

Salidas:
  catalogo_mandarina
  final_cost

Validaciones:
- quantity > 0.
- product_name no vacío tras strip().
- Verificar si product_name está en el diccionario (clave).

Casos:
  We have this products: camote, chamoy, papa, choripan
  The price of this products are: {'camote': 15.99, 'chamoy': 17.5, 'papa': 27.99, 'choripan': 30.5}
  What are you buy? ("end" to exit) camote
  How much do you want? 7
  What are you buy? ("end" to exit) chamoy
  How much do you want? 3
  What are you buy? ("end" to exit) end
  {'camote': 7, 'chamoy': 3}
  164.43

  We have this products: camote, chamoy, papa, choripan
  The price of this products are: {'camote': 15.99, 'chamoy': 17.5, 'papa': 27.99, 'choripan': 30.5}
  What are you buy? ("end" to exit) a
  This product is NOT in sell
  What are you buy? ("end" to exit) end
  {}
  0.0

  We have this products: camote, chamoy, papa, choripan
  The price of this products are: {'camote': 15.99, 'chamoy': 17.5, 'papa': 27.99, 'choripan': 30.5}
  What are you buy? ("end" to exit) PAPA
  How much do you want? a
  type error
  {}
  0.0
"""
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

"""
Entradas:
  who_student

Salidas:
  califications
  average

Validaciones:
- student_name no vacío tras strip().
- Verificar si student_name es una clave en el diccionario.
- Verificar que la lista de calificaciones no esté vacía antes de calcular el promedio.

Casos:
  The students are Edson Rodrigo Humberto
  Who student's calification You want? Edson
  The studen Edson califications are: [8.5, 9, 10]
  The average of this student is 9.166666666666666

  The students are Edson Rodrigo Humberto
  Who student's calification You want? HUMBERTO
  The studen HUMBERTO califications are: [10, 9.5, 8.4]
  The average of this student is 9.299999999999999

  The students are Edson Rodrigo Humberto
  Who student's calification You want? Hittler
  This student is NOT in the list
"""

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

"""
Entradas:
  setence

salidas:
  frequence

Validaciones:
- sentence no vacía tras strip().
- Manejar signos de puntuación simples si el estudiante decide hacerlo (documentar su decisión, por ejemplo usando replace()).
- Verificar que la lista de palabras no esté vacía.

Casos:
  set your setence: this is a test this is only a test
  {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}

  set your setence: hello world hello everyone
  {'hello': 2, 'world': 1, 'everyone': 1}

  set your setence: one fish two fish red fish blue fish
  {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}

"""

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

"""
Entradas:
  option
    contact
    number

Salidas:
  contact_book

Salidas:
- Para "ADD":
  - "Contact saved:" name, phone
- Para "SEARCH":
  - Si existe: "Phone:" <phone>
  - Si no existe: "Error: contact not found"
- Para "DELETE":
  - Si existe: "Contact deleted:" name
  - Si no existe: "Error: contact not found"

Casos:
  Set 1 to add or modify a contact
  Set 2 to search a contact
  Set 3 to remove a contact
  Set 4 to show the list of contacts
  What do you want? 1
  Name of contact: Edson
  number of contact 834 124 5678
  You add a EDSON (834 124 5678) to contact book
  Do you finish? Yes/No no

  Set 1 to add or modify a contact
  Set 2 to search a contact
  Set 3 to remove a contact
  Set 4 to show the list of contacts
  What do you want? 2
  Name of contact: EDSON
  The number of EDSON is 834 124 5678
  Do you finish? Yes/No no

  Set 1 to add or modify a contact
  Set 2 to search a contact
  Set 3 to remove a contact
  Set 4 to show the list of contacts
  What do you want? 4
  EDSON : 834 124 5678
  Do you finish? Yes/No

  Set 1 to add or modify a contact
  Set 2 to search a contact
  Set 3 to remove a contact
  Set 4 to show the list of contacts
  What do you want? 1
  Name of contact: Charly
  number of contact 3184400
  You add a CHARLY (3184400) to contact book
  Do you finish? Yes/No no'

  Set 1 to add or modify a contact
  Set 2 to search a contact
  Set 3 to remove a contact
  Set 4 to show the list of contacts
  What do you want? 3
  Name of contact: Edson
  Do you finish? Yes/No no

  Set 1 to add or modify a contact
  Set 2 to search a contact
  Set 3 to remove a contact
  Set 4 to show the list of contacts
  What do you want? 4
  CHARLY : 3184400
  Do you finish? Yes/No yes
"""

"""
Conclusión:
  Como conclusion, en esta actividad aprendi a usar listas, tuplas y diccionarios de 
  mejor manera, cosa que me ayudara en un futuro a la hora de programar y organizar 
  los datos y la informacion que se maneja en los programas, aumentando mi eficiencia
  y productividad al momento de programar.

Referencias:
https://docs.python.org/3/tutorial
https://www.w3schools.com/python/python_lists.asp
https://www.w3schools.com/python/python_tuples.asp
https://www.w3schools.com/python/python_dictionaries.asp
Google IA
"""