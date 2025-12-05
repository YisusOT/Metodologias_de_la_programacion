"""
Jesus Ignacio Olvera Trejo

Grupo IM 1-2

Matricula: 2530266

Descripción:
Implementa un programa en Python que gestione un conjunto de "items" en memoria mediante operaciones CRUD. 
Cada ítem puede representar, por ejemplo, un producto de inventario con los siguientes campos sugeridos:
- id (string o int, único)
- name (string)
- price (float)
- quantity (int)

"""


data_base = {
  'chamoy' : {
    "ip" : 0,
    "quantity" : 4,
    "price" : 12.5
  },
  'camote' : {
    'ip' : 1,
    "quantity" : 3,
    "price" : 10.0
  },
}
data = {}
ip = 1
option = 's'
while option != 'exit': 
  print('Set 1 to add')
  print('Set 2 to read')
  print('Set 3 to update')
  print('Set 4 to delete')
  print('Set 5 to show all items')
  print('Set "exit" to exit')
  option = input('').strip()
  if option == '1': 
    data = {}
    product = input('set the name of the product ')
    quantity = int(input('Set the quantity: '))
    price = float(input('Set the price: '))
    data['price'] = price
    data["ip"] = ip + 1
    data['quantity'] = quantity
    data_base[product.lower()] = data
  elif option == '2':
    print(data_base.keys())
    product = input('set the product to read: ').lower().strip()
    if product in data_base:
      print(data_base[product])
    else:
      print('Set a real product')
  elif option == '3':
    print(data_base.keys())
    product = input('set the product to read: ').lower().strip()
    if product in data_base:
      print(data_base[product])
      quantity = int(input('Set the new quantity: '))
      price = float(input('Set the new price: '))
      data_product = data_base[product]
      data_product['quantity'] = quantity
      data_product['price'] = price
      data_base[product] = data_product
    else:
      print('Set a real product')

  elif option == '4':
    print(data_base.keys())
    product = input('set the product to read: ').lower().strip()
    if product in data_base:
      data_base.delete(product)
    else:
      print('Set a real product')

  elif option == '5':
    print(data_base)

  elif option == 'exit':
    print('You exit the program')
    break

"""
Entradas:
  option: str
  product: str
  quantity: int
  price: float

Salidas:
  data_base: dict
  data: dict

Variables:
  ip: int
  data_product: dict

Validaciones:
Validaciones:
- option debe ser una de las opciones definidas (por ejemplo 0–5).
- item_id no vacío tras strip().
- price y quantity deben ser números válidos:
  - price >= 0.0
  - quantity >= 0
- Si falla alguna validación, mostrar "Error: invalid input" y NO realizar la operación.
- En CREATE:
  - Si el id ya existe, decide una política (por ejemplo, no permitir duplicados) y documenta tu elección.
- En READ/UPDATE/DELETE:
  - Si el id no existe, mostrar "Item not found".

"""
"""
Conclusión:
  En conclusion, gracias a este trabahi aprendi que es CRUD y como se implementa en python, siendo CRUD un
  acronimo de Create, Read, Update y Delete, que son las operaciones basicas para el manejo de datos en una
  base de datos. Ademas, aprendi a manejar diccionarios en python para almacenar y manipular los items en memoria.

Referencias:
  https://www.w3schools.com/python/python_dictionaries.asp
  https://www.codecademy.com/article/what-is-crud-explained
  https://typethepipe.com/es/post/diccionario-en-python
  https://realpython.com/python-crud-app/
  https://www.programiz.com/python-programming/dictionary
"""