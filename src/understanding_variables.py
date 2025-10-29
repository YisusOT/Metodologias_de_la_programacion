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
print(charly_mesage, another_message)

""" 
traceback: es un registro donde el interprete tuvo problemas para ejecutar su codigo
    
    Traceback (most recent call last):
    File "C:\Users\jesus\projects\Metodologias_de_la_programacion\src\understanding_variables.py", line 25, in <module>
        print(charly_mesage, another_message)
            ^^^^^^^^^^^^^
    NameError: name 'charly_mesage' is not defined. Did you mean: 'charly_message'?

Name error: significa que olvidamos establecer el valor de la variable antes de usarlo o cometimos un error al ingresar el nombre de la variable




"""