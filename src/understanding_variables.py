message = "This is my first python variable"
another_message = 'I am really, really, really happy'
# print () -> use to show messages in terminal
print(message)
print(another_message)
print(message, another_message, message)
message = 'Chamoy'
print(message)
""" 
Los nombres de variables en python deben nombrarse solo con:
    - Letras, numeros y guion bajo (espacios)
    - Deben comenzar con una letra o con guion bajo, pero NO con numeros
        ejemplo correcto: message_1
        ejemplo incorrecto: 1_message
    - no utilizar espacios para separar palabras en kis nombres de las variables
    - no utilizar palabras reservadas de python para nombrar variables o archivos
        print
    - los nombres deben ser cortos, pero descriptivos
    - los nombres deben ser en ingles
    - nombres de variables en minusculas
    - nombres de constantes en mayusculas
"""

charly_message = "Hola, soy charly y"
print(charly_message, another_message)

"""
traceback: es un registro donde el interprete tuvo problemas para ejecutar su codigo
    
    Traceback (most recent call last):
    File "C:/Users/jesus/projects/Metodologias_de_la_programacion/src/understanding_variables.py", line 25, in <module>
        print(charly_mesage, another_message)
            ^^^^^^^^^^^^^
    NameError: name 'charly_mesage' is not defined. Did you mean: 'charly_message'?

Name error: significa que olvidamos establecer el valor de la variable antes de usarlo
 o cometimos un error al ingresar el nombre de la variable

Un string es de manera sencilla una serie de caracteres.
En Python todo lo que se encuentre dentro de comillas simples '' o comillas dobles "" es considerado un string
    "Esto es un string"
    'Esto tambien es un string'

    'Le dije a un amigo, "!Phyton es mi lenguaje favorito"'
    "el lenguanje 'python' lleva el nombre por Monty Phyton, no por la serpiente"
hola

"""

name = "clase de programacion"
print(name)
print(name.title())

"""
Un metodo es una accion que python puede realizar en un fragmento de datos o sobre una variable.
El punto . despues de una variable seguida del metodo .title() dice que se tiene que ejecutar el metodo .title()
de la variable name

Todos los metodos van seguidos de un parentesis porque en ocaciones se necesitan informacion adicional para funcionar
lo cual iria dentro de los parentesis
En esta ocacion el metodo .title() no requiere informacion adicional para ejecutarse.
"""

print(name.lower())
print(name.upper())

#Concatenacion de strings
print("Concatenacion de strings")
first_name = "Charly"
last_name = "mercury"
full_name = first_name + " " + last_name
print(full_name)

print("Hola, " + full_name.title() + "!")

print("  ")
print("  ")
print("  ")
print("  ")

#Syntax error con strings
message = "Una fortaleza de 'python' es su comunidad"
print(message)

print("  ")

# Concatenacion convencional
famous_person = "Charly mercury"
quote = "Python is love"
message = famous_person + " una vez dijo " + quote
print(message)

# concatenacion con fstring
message_f_string = f"{famous_person} una vez dijo {quote}"
print(message_f_string)

# actividad

""" 
1) Elige un personaje famoso e igualalo a una variable de tipo string
2) Elige una frase famosa que haya dicho e igualalo a una variable de tipo string
3) Genera un mensaje con las 2 variables usando fstring
4) Imprime el mensaje
"""

famous_person = "Beto"
quote = "'Ya viste lo que hacen los de tu etnia'"
message = f"{famous_person} una vez dijo {quote}"
print("  ")
print("  ")
print(message)
print("  ")
print("  ")