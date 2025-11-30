"""
Jesus Ignacio Olvera Trejo

Grupo IM 1-2

Matricula: 2530266

"""

# Problema 1:
print('Problema 1\n')
"""
Dado el nombre completo de una persona en una sola cadena (por ejemplo: "juan carlos tovar"), el programa debe:
1) Normalizar el texto (strip, espacios extra, mayúsculas/minúsculas).
2) Mostrar el nombre formateado en Title Case y las iniciales (por ejemplo: J.C.T.).
"""
first_name = str(input('Set your first name'))
last_name = str(input('Set your last name'))
full_name = first_name.strip() + " " + last_name.strip()
print(f'your name is {full_name.upper()}')
print(f'your name is {full_name.lower()}')
letters = first_name[0].upper() + ' ' + last_name[0].upper()
print(letters)

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
    if email.find('.') > email.find('@'):
        print('vyour email is correct')
    else:
        print('your email is incorrect')
else:
    print('your email is incorrect')

# Problema 3:
print('\n\n\nProblema 3\n')
"""
Descripción:
Determina si una frase es un palíndromo, es decir, se lee igual de izquierda a derecha y de derecha a izquierda, ignorando espacios y mayúsculas/minúsculas.
"""
setence = str(input('Set your setence '))
true_setence = setence.replace(' ', '')
list_1 = list(true_setence)
print(list_1)
list_2 = []
for value in list_1:
    list_2.insert(0, value)
print(list_2)
if list_1 == list_2:
    print('Your setence is polindromo')
else:
    print('Your setence is NOT palindromo')

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
setence = str(input('Set your setence '))
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
  print(digits)
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
  print('upper')
if lower_letter:
  level = level + 1
  print('lower')
if numer:
  level = level + 1
  print('numero')


if level == 0 or level == 1:
  print('your passsword is weak')
elif 2 <= level <= 3:
  print('your password is medium')
elif level >= 4:
  print('your password is strong')
else:
  print('camote')

print(level)

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
print(len(final))