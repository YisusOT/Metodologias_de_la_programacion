cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw'
        print(car.upper())
    else:
        print(car)
# El condicional es el corazon de un if

# Condicional True

car = 'bmw'
print(car == 'bmw') # True

# Condicional False

car = 'Audi'
print(car == 'audi')

# Posible solucion a entradas de usuario

print(car.lower() == 'audi')

# Operador racional != para determinar desigualdad
requested_topping = 'mushroom'
if requested_topping != 'anchovies':
    print('hold the anchovies')

# Comparaciones numericas
age = 18
print(age == 18)
answer = 17
if answer != 42:
    print('Intenta otra vez, esa no es la respuesta correcta')

age = 17
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

# Multiples condiciones
# operacion and
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >=21) # False
print(age_0 >= 21 and age_1 >=18) # True
# operacion or 
print(age_0 >= 21 or age_1 >=21) # True
print(age_0 >= 23 or age_1 >=18) # True

"""
Para preguntarnos si un valor especifico esta en una lista podemos utilizar el siguiente comparador
value in list
"""

motorcycles = ['mortalica', 'honda', 'vento', 'yamaha']
moto_charly_wants = 'italica'
print(moto_charly_wants in motorcycles) # False
print('honda' in motorcycles) # true

"""
Para preguntarnos si un valor especifico NO esta en una lista podemos utilizar el siguiente comparador
value not in list
"""

banned_students = ['jorge', 'carlos', 'moyra', 'luz', 'hots']
user = 'mauro'
print(user not in banned_students) # True
print('jorge' not in banned_students) # False

# variables de tipo booleano
game_active = True
can_edit = False

"""
if statements
sintax:

if condition:
    do something


if condition:
    do something
else:
    do something


"""