"""
functions
    Las funciones son bloques de codigo diseñados para realizar una tarea especifica

    Cuando queremos realizar una tarea que se ha definido en un a funcion, tenemos que llenar el nombre
    de la funcion responsable de esto.

    Definicion de una funcion (Syntax)

    - def name_of_function(parametros):
        actions
"""
# sin parametros
def greet_mauro():
    print('hola mauro')

# Con 2 parametros
def greet(user_name, msj):
    print(f'hola {user_name}, {msj} chamoy')

# Argumentos
# greet('Jhordan', 'camote')
# greet_mauro()


"""
Un programa que genere el nombre completo de una persona

Vamos a darle el primer nombre, segundo y apellido

La funcion debe generar el nombre completo y regresarlo
"""

def create_full_name(first_name, last_name, middle_name=''):
    """
    Docstrings: 
        "Esta funcion crea el nombre completo" 
    """
    full_name = f'{first_name} {middle_name} {last_name}'
    return full_name.title()

user_first_name = input('Set your first name; ').strip().lower()
user_middle_name = input('Set your middle name; ').strip().lower()
user_last_name = input('Set your last name: ').strip().lower()

# Argumentos posicionales
create_full_name(
    user_first_name, 
    user_middle_name, 
    user_last_name)
full_name = create_full_name(user_first_name, user_middle_name, user_last_name)

print(full_name)

# Argumetos c lave -> keyboard arguments
full_name_key = create_full_name(
    last_name= user_last_name,
    first_name= user_first_name,
    middle_name= user_middle_name
)
print(full_name_key)

# parametros opcionales
profe_falso = create_full_name(user_first_name, user_last_name)
print(profe_falso)

# Temas para estudiar a futuro
"""
args, kwargs en funciones
manejo de datos: abrir archivos csv, .json, .yml, .txt, 
argumentos por lineas de comando - sys
cli - command line interface
generadores, iteradores, yield
testing -> 
"""