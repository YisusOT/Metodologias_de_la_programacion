"""
Las listas tambien pueden almacenar numeros, y de echo son ideales para almacenarlos. 
Python ofrece cantidad de funciones integradas para trabajar con listas de numeros:
    Por ejemplo, funcion range(): 

"""
# La funcion range() genera una lista de numeros en un rango especifico
numbers = list(range(10))  #genera numeros de 0-9
print(numbers)

# Podemos realizar lo mismo con un for loop:

for num in range(10):
    print(num)

print(" ")
print(" ")
for num in range(1, 5):
    print(num)
print(" ")
print(" ")
for num in range(1, 10, 2):
    print(num)
print(" ")
print(" ")
for num in range(2, 10, 2): # range(comienzo, fin-1, salto entre numeros)
    print(num)

# Podemos crear cualquier tipo de lista con numeros

print("\n primeros 10 numeros al cuadrado: \n")
squares = []
for value in range(1, 11):
    square = value **2
    squares.append(square)
print(squares)

# Metodos built in para listas de numeros
print("\n Metodos built-in\n")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("lista de digitos: ", digits)
print(min(digits))
print(max(digits))
print(sum(digits))

print(" ")

square_list_zip = [num**2 for num in range(10)]
print(square_list_zip)