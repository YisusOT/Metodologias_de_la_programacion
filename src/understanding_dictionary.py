""""
Estructura de diccionario:
    Lista = {key: value , key_2: value_2 , ... key_n: value_n}
"""

# Diccionario simple
alien_0 = {'color': 'green' , 'points': 5}

#Diccionario mas simple
alien_1 = {'color': 'yellow'}

# Acceso a diccionarios
print(alien_0['points'])  # Salida: 5
print(alien_1['color'])   # Salida: yellow


print('\n\n\n')


# Diccionario vacío
alien_2 = {}
# Llenar un diccionario
alien_2 = {'color': 'yellow'}
alien_2['color'] = 'blue'
# Agregar nuevas llaves
alien_2['name'] = 'chamoy'
alien_2['edad'] = 25

print(alien_2)


print('\n\n\n')

# uso: almacenar valores similares
favorite_language = {
    'jen': 'phyton',
    'sara': 'c',
    'edward': 'ruby',
    'phil': 'phyton', 
}
# Looping
print('\n')
for key, value in favorite_language.items():
    print(f"{key.title()}'s favorite language is {value.title()}")
print('\n')
for key in favorite_language.keys():
    print(key)
print('\n')
for value in favorite_language.values():
    print(value)    

# Nesting dictionary / dentro de diccionarios 

## Listas en diccionarios

## Listas de diccionarios

## diccionarios dentro de listas
covenant_jackal = {
    "color" : 'gray',
    "weapon" : 'plasma_sword',
    'armament' : 'plasma grande', 
    'health' : 5, 
}

covenant_elite = {
    'COLOR' : 'verde',
    'weapon' : 'gun'
}

covenant_grunt = {
    'color' : 'azul',
    'healt' : 10
}

covenants = [
    covenantn_jackal,
    covenant_elite,
    covenant_grunt,
]

for covenant in covenants: # Abre lista de diccionarios
    print('\n', covenant)
    for key, value in covenant: # abre el diccionario de la lista
        print(key, value)
    print()




# Listas en diccionarios

students = {
    "jorge" : ['chamoy', 'aprobado'],
    'lizarriturri' : ['camote', 'reprobado'],
    'isac' : ['merequetengue', 'aprobado2']
}

# Diccionarios en diccionarios

Sensores = {
    'temperatura' = {
        'id' = 'tem',
        'value' = 5,
        'ubi' = 'aula 104',
    },
    'humedad' = {
        'id' = 'hum',
        'value' = 35,
        'ubi' = 'aula 105',
    },
}