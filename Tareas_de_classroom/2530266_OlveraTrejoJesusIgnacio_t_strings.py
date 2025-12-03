"""
Jesus Ignacio Olvera Trejo

Grupo IM 1-2

Matricula: 2530266

"""

# Problema 1: Full name formatter (name + initials)
print('Problema 1\n')
"""
Dado el nombre completo de una persona en una sola cadena (por ejemplo: "juan carlos tovar"), el programa debe:
1) Normalizar el texto (strip, espacios extra, mayúsculas/minúsculas).
2) Mostrar el nombre formateado en Title Case y las iniciales (por ejemplo: J.C.T.).
"""
full_name = input('Set your name: ')
true_name = full_name.strip().title()
list_name = list(true_name.split())
letters = []
for name in list_name:
  letters.append(name[0:1])
letter = ".".join(letters)
names = " ".join(list_name)
print(f'Your full name is {names}')
print(f'Your initials are {letter}')
"""
Entradas:
  full_name

Salidas:
  names
  letters

Validaciones:
- full_name no debe estar vacío después de strip().
- Debe contener al menos dos palabras
- No aceptar cadenas que sean solo espacios.


Casos:
  Set your name: JesUs      IgNacIo OlvEra Trejo
  Your full name is Jesus Ignacio Olvera Trejo
  Your initials are J.I.O.T

  Set your name: 5675 Olvera  Trejo
  Your full name is 5675 Olvera Trejo
  Your initials are 5.O.T

  Set your name: %653# Jesus              IgnACio
  Your full name is %653# Jesus Ignacio
  Your initials are %.J.I
"""

# Problema 2
print('\n\n\nProblema 2\n')
"""
Valida si una dirección de correo tiene un formato básico correcto:
- Contiene exactamente un '@'.
- Después del '@' debe haber al menos un '.'.
- No contiene espacios en blanco.
Si el correo es válido, también muestra el dominio (la parte después de '@').
"""
email = str(input('Set your email: '))
if '@' in email and '.' in email and ' ' not in email :
    if email.count('@') == 1:
        print('your email is correct')
    else:
        print('your email is incorrect')
else:  
    print('your email is incorrect')

"""
Entradas:
  email

Salidas:
  boolean:
    True: email is correct
    False: email is incorrect
  
Validaciones:
- email_text no vacío tras strip().
- Contar cuántas veces aparece '@'.
- Verificar que no haya espacios (no debe haber " " en email_text

Casos:
  Set your email: Jesus@gmail.com
  your email is correct

  Set your email: chamoy.j@camote
  your email is incorrect

  Set your email: Jesus.chamoy@gmail
  your email is incorrect
"""

# Problema 3:
print('\n\n\nProblema 3\n')
"""
Descripción:
Determina si una frase es un palíndromo, es decir, se lee igual de izquierda a derecha y de derecha a izquierda, ignorando espacios y mayúsculas/minúsculas.
"""
setence = str(input('Set your setence '))
true_setence = setence.replace(' ', '')
list_1 = list(true_setence.lower())
print(list_1)
list_2 = []
for value in list_1:
    list_2.insert(0, value)
print(list_2)
if list_1 == list_2:
    print('Your setence is polindrome')
else:
    print('Your setence is NOT palindrome')

"""
Entrada:
  setence

salida:
  list_1
  list_2 # list_1 reverseado
  Boolean:
    True: Your setence is polindromo
    False: Your setence is NOT polindromo

Validaciones:
- phrase no vacía tras strip().
- Longitud mínima razonable después de limpiar espacios (por ejemplo, al menos 3 caracteres).

Casos:
  Set your setence Anita lava la tina
  ['a', 'n', 'i', 't', 'a', 'l', 'a', 'v', 'a', 'l', 'a', 't', 'i', 'n', 'a']
  ['a', 'n', 'i', 't', 'a', 'l', 'a', 'v', 'a', 'l', 'a', 't', 'i', 'n', 'a']
  Your setence is polindromo

  Set your setence 545
  ['5', '4', '5']
  ['5', '4', '5']
  Your setence is polindromo

  Set your setence Chamoy
  ['c', 'h', 'a', 'm', 'o', 'y']
  ['y', 'o', 'm', 'a', 'h', 'c']
  Your setence is NOT palindromo
""" 

# Problema 4
print('\n\n\nProblema 4\n')

"""
Descripción:
Dada una oración, el programa debe:
1) Normalizar espacios (quitar espacios al principio y al final).
2) Separar las palabras por espacios.
3) Mostrar:
   - Número total de palabras.
   - Primera palabra.
   - Última palabra.
   - Palabra más corta y más larga (por longitud).

"""
setence = str(input('Set your setence: '))
right_setence = setence.strip()
letters = setence.replace(' ', '')
num_of_words = right_setence.count(' ') + 1
words = right_setence.split()
first_word = words[0]
last_word = words[-1]
smallest_word = min(words, key=len)
langer_word = max(words, key=len)
print(f'the setence have {num_of_words} words')
print(f'the first word of the setence is {first_word}')
print(f"The last word is {last_word}")
print(f"The smallest word is {smallest_word}")
print(f"the langer word is {langer_word}")

"""
Entrada:
  setence

Salida:
  num_of_words
  first_word
  last_word
  smallest_word
  langer_word

Validaciones:
- Oración no vacía tras strip().
- Debe contener al menos una palabra válida después de split().

Casos:
  Set your setence: Una vez comi un taco
  the setence have 5 words
  the first word of the setence is Una
  The last word is taco
  The smallest word is un
  the langer word is comi

  Set your setence: Anita lava la tina
  the setence have 4 words
  the first word of the setence is Anita
  The last word is tina
  The smallest word is la
  the langer word is Anita

  Set your setence: Hittler es mi idolo #1 :)
  the setence have 6 words
  the first word of the setence is Hittler
  The last word is :)
  The smallest word is es
  the langer word is Hittler
"""

# Problema 5:
print('\n\n\n Problema 5:\n ')
"""
Clasifica una contraseña como "weak", "medium" o "strong" según reglas mínimas 
(puedes afinarlas, pero documéntalas en los comentarios).
"""
level = 0
upper_letter = False 
lower_letter = False
numer = False
try:
  password = input('Set your password to evaluate: ')
  digits = list(password)
  for digit in digits:
    if digit.isnumeric():
      int(digit)
      numer = True  # Si contiene 1 numero, el nivel aumenta en 1
    elif digit.isalpha:
      if digit.isupper():
        upper_letter = True # Si tiene una minuscula, el nivel aumenta en 1
      elif digit.lower():
        lower_letter = True # Si tiene mayuscula, el nivel aumenta en 1
except:
  print('algo falló xd')

if len(password) >= 8: # Si tiene 8 o mas caracteres, el nivel aumenta en 1
    level = level + 1
if upper_letter:
  level = level + 1
if lower_letter:
  level = level + 1
if numer:
  level = level + 1

if level == 0 or level == 1:
  print('your passsword is weak')
elif 2 <= level <= 3:
  print('your password is medium')
elif level >= 4:
  print('your password is strong')
else:
  print('camote')
print(level)

"""
Entrada:
  password

Salida:
  level_of_password

Validaciones:
- No aceptar contraseña vacía.
- Verificar longitud con len().

Casos:
  Set your password to evaluate: chamoy
  your passsword is weak

  Set your password to evaluate: Camote67
  your password is strong

  Set your password to evaluate: Choripan
  your password is medium
"""

# Problema 6:
print('\n\n\n\Problema 6:\n')
"""
Descripción:
Dado el nombre de un producto y su precio, genera una etiqueta en una sola línea con el siguiente formato:

Product: <NAME> | Price: $<PRICE>

La cadena completa debe tener exactamente 30 caracteres:
- Si es más corta, rellena con espacios al final.
- Si es más larga, recorta hasta 30 caracteres.
"""

product = input('Name of the product: ')
price = input('Price of product: ')
final_product = f'Product: {product} | Price: {price}$'
if len(final_product) == 30:
  print(final_product)
  print('30')
elif len(final_product) < 30:
  points = 30 - len(final_product)
  point = []
  for value in range(points):
    value = ' '
    point.append(value)
  punto = "".join(point)
  final = (f"Product: {product} {punto}| Price: {price}$")
else:
  final = final_product[0:30]
print(final)
lenght_final = len(final)
print(f"The lenght is {lenght_final}" )

"""
Entrada:
  product
  price

Salidas:
  final_product
  len(final_product)

Validaciones:
- product_name no vacío tras strip().
- price_value debe poder convertirse a un número positivo.


  Name of the product: Chamoy
  Price of product: 43
  Product: Chamoy   | Price: 43$
  The lenght is 30

  Name of the product: camote
  Price of product: cincp
  Product: camote | Price: cincp
  The lenght is 30

  Name of the product: Merequetengue
  Price of product: 6
  Product: Merequetengue | Price
  The lenght is 30
"""

"""
Conclusion:
  Para concluir, gracias a este trabajo aprendi muchas funciones que 
  se pueden aplicar a los strings, desde agreagarlos a listas hasta
  como razonar para poder resolver los problemas

Referencias:
https://www.datacamp.com/es/tutorial/python-split-list
https://www.ionos.com/es-us/digitalguide/paginas-web/desarrollo-web/python-string-to-list/
https://www.datacamp.com/es/tutorial/python-string-tutorial
https://labex.io/es/tutorials/python-how-to-replace-multiple-whitespaces-in-a-python-string-417565
https://es.stackoverflow.com/questions/412359/
  eliminar-saltos-de-linea-dentro-de-una-lista-leo-un-archivo-nombre-numero-tel
"""