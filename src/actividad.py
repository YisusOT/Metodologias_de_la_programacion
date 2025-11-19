"""
Hacer un programa que pregunte la edad de la persona y responda lo siguiente:
    - si la edad es menor o igual a 4, la entrada es gratuita 
    - si es mayor a 4 y menor o igual a 18, entonces la entrada cuesta 200
    - si es mayor a 18 entonces cuesta 400
"""

try:
    age = int(input("Set your age: "))
    if age >= 18:
        print("La entrada cuesta 400$")
    elif age < 18 and age > 4:
        print("la entrada cuesta 200$")
    elif age <= 4 and age >= 0:
        print("La entrada es gratuita")
    else:
        print("Ingresa un año real")
except:
    print("Ingresa un numero real")