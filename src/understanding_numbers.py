# Numbers
print(" ")
"""
    Integers = enteros
        Ejemplo, una variable de tipo entero seria:
        # Tipado dinamico
            age = 23
        Los podemos sumar (+), restar (-), multiplicar (*) y dividir (/)
        potencias (**N, **2)
        Modulo (divideindo % divisor)
"""
number_1 = 33
number_2 = 13
suma = number_1 + number_2
diference = number_1 - number_2
multiplication = number_1 * number_2
division = number_1 / number_2
modulo = number_1 % number_2
power = number_1 ** number_2
print("Suma = ", suma)
print("diferencia = ", diference)
print("multiplicacion = ", multiplication)
print("division = ", division)
print("modulo = ", modulo)
print("power = ", power)

print(" ")
print(" ")
print(" ")

print("Suma es del tipo ", type(suma))
print("diferencia es del tipo ", type(diference))
print("multiplicacion es del tipo ", type(multiplication))
print("division es del tipo ", type(division))
print("modulo es del tipo ", type(modulo))
print("power es del tipo ", type(power))


# Flotantes = Float

print(" ")
print(" ")
print(" ")

"""
    Float = Reales
        Ejemplo, una variable de tipo real seria:
        # Tipado dinamico
            age = 23.6
        Los podemos sumar (+), restar (-), multiplicar (*) y dividir (/)
        potencias (**N, **2)
        Modulo (divideindo % divisor)
"""

### Imprimir la edad de alguien
"""
age = 33
message = "Charly tiene " + age + " años "
print(message)

    Con este codigo arroja un TypeError porque estamos juntando un numero con texto y python
    no puede reconocer el tipo de informaion que se esta usando

    Para convertir a string utilizo: str()
"""
age = 33
message_f = f"Charly tiene {age} años"
print(message_f)

message = "Charly tiene " + str(age) + " años "
print(message)

print(" ")