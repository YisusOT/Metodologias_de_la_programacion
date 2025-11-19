"""
Vamos a realizar un programa que pregunte la edad al usuario y muestre un mensaje diferente segun el rango
de edad en el que se encuentre
"""
try:
    age = int(input("Set your age "))

    if age >= 18 and age <100:
        print("You are adult")
    elif age < 18 and age >= 0:
        print("you are young")
    elif age >= 100:
        print("tienes mas de un siglo de edad ")
    else:
        print("your age is negative")
except:
    print("tuviste un error")

print("\nChamoy")

guisos = ["deshebrada", "asado", "salsa verde", "pozole"]
if "asado" in guisos:
    print("si hay asado")
else:
    print("no hay asado")
if "tamales" in guisos:
    print("Hay tamales")
else:
    print("no hay tamales")
if "salsa verde" in guisos:
    print("hay salsa verde")
else:
    print("no hay salsa verde")