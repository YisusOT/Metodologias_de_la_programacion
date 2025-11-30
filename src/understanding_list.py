# Listas
# Una lista es una coleccion ordenada y mutable de elementos
# Se definen utilizando corchetes [] y separando los elementos con comas
print(" ")
print(" ")

fruits = ['manzana', 'banana', 'cereza' ]
print(fruits) #Salida = "['manzana', 'banana', 'cereza']"

print(" ")

print(fruits[0])
print(fruits[1].upper())
print(fruits[2].title())

print(" ")
print(" ")

print(fruits[-1].capitalize())
print(fruits[-2].lower())
print(fruits[-3])
# Los negativos seleccionas los ultimos, -1 el ultimo, -2 el penultimo, etc.

print(" ")
print(" ")

message = f'Mi fruta favorita es {fruits[0].title()}'
print(message) 

print(" ")
print(" ")

# Metodos de listas
"""
agregar elementos a una lista
    - append() : agrega un elemento al FINAL de la lista, este metodo ocupa un solo argumento
    (element) el cual es el elemento que se desea agregar a la lista.
"""
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

print(" ")
print(" ")

motorcycles.append('ducati')
print(motorcycles)

print(" ")
print(" ")

"""
agregar elementos en una posicion especifica
    - insert()
    Este metodo ocupa 2 argumentos (index, element): el indice donde se desea insertar el
    elemento y el elemento en si
"""
motorcycles.insert(-2, 'chamoy')
print(motorcycles)

print(" ")
print(" ")
print(" ")
print(" ")

"""
Eliminar metodos de una lista
    - del: Elimina un elemento de una posicion especifica de la lista.
    La declaracion del index elimina el elemento en la posicion especificada

    - pop(): Elimina y devielve el ultimo elemento de la lista.
    no requiere argumentos y elimina el ultimo elemento de la lista

    - pop(index): elimina y devuelve un elemento en una posicion especifica de la lista
    El metodo toma un argumento, que es el indice del elemento que se desea eliminar y devoler

    - Remove(): Elimina la primera aparicion de un valor especifico de la lista
    Usa un argumento (value) donde es el valor del elemento que se desea eliminar
"""
print(motorcycles)
del motorcycles[1]
print(motorcycles) # Salida = ['honda', 'yamaha', 'chamoy', 'suzuki', 'ducati']
pop_motorcycles = motorcycles.pop()
print(motorcycles) # Salida = ['honda', 'chamoy', 'suzuki']
print(f'la moto eliminada es: {pop_motorcycles}' ) # salida = la moto eliminada es: ducati

print(" ")
second_motorcycles = motorcycles.pop(1)
print(motorcycles)
print(f'la moto eliminada es: {second_motorcycles}')

print(" ")
print(motorcycles)
motorcycles.remove('suzuki')
print(motorcycles)

print(" ")
print(" ")
print(" ")
print(" ")

names = ['ana', 'juan', 'pedro', 'maria', 'jose']
print(names)
del_name = input("Ingrese el nombre que desea eliminar de la lista:  ")
names.remove(del_name.strip().lower())
print(names)

print(" ")
print(" ")
print(" ")
print(" ")

"""
    Como ordenar listas en Python
    -sort() : Ordena la lista de forma permanente en orden ascendente o descendente

        Ordenamiento permanente, es decir, ordena la lista original y no crea una nueva lista ordenada.
        Por defecto, sort() ordena en orden ascendente (de menor a mayor).

        sort(reverse=True) : Ordena la lista en orden descendente (de mayor a menor).
        sort(reverse=False) : Ordena la lista en orden ascendente (de menor a mayor
"""
print("\n Como ordenar listas en Python \n".capitalize())
cars = ['bmw', 'audi', 'toyota', 'kia', 'ford', ]
print(cars)  # Salida: ['bmw', 'audi', 'toyota', 'kia', 'ford']
cars.sort(reverse=False)  # Ordena la lista en orden ascendente
print(cars)  # Salida: ['audi', 'bmw', 'ford', 'kia', 'toyota']

motorcycles = ["mortalica","honda","ducatti"]
print(motorcycles)
motorcycles.reverse()
print(motorcycles) # Salida: ['ducatti', 'honda', 'mortalica']

"""
    Cantidad de elementos en una lista
    Metodo built-in len() : Devuelve la cantidad de elementos en una lista
"""
cars = ['ford', 'kia', 'chevrolet']
print("\n Metodo built-in len() \n")
print(len(cars))  # Salida: 3


"""
    Metodo built-in
    Ordena las listas temporalmente sin modificar la lista original
    -sorted() : Ordena la lista temporalmente en orden ascendente o descendente
        sorted(lista) : Ordena la lista en orden ascendente (de menor a mayor)
        sorted(lista, reverse=True) : Ordena la lista en orden descendente (de mayor a menor)
        sorted(lista, reverse=False) : Ordena la lista en orden ascendente (de menor a mayor)
"""
favorite_students = ["jorge", "jose","carlos","emiliano"]
print(favorite_students)  # Salida: ['jorge', 'jose', 'carlos', 'emiliano']

fav_stu_ordened = sorted(favorite_students, reverse=False)  # Ordena la lista en orden ascendente
print("lista ordenada: ",fav_stu_ordened)  # Salida: lista ordenada:  ['carlos', 'emiliano', 'jorge', 'jose']
print("lista original: ",favorite_students)  # Salida: lista original:  ['jorge', 'jose', 'carlos', 'emiliano']
