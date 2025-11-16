# List comprehensions
print("\n\n")
"""
Una list comprehensions combina el for loop y la creacion de nuevos elemento s en una sola linea de codigo y tambien 
automaticamente agreaga el nuevo elemento a la lista, es decir, sin usar el appent
"""
squares = [value**2 for value in range(1, 11)]
print(squares)
print("\n\n")

# Numeros pares con range
even_numbers_0_100 = list(range(0, 101, 2))
print(even_numbers_0_100)

# numeros pares usando list compre...
evens_list_zip = [value for value in range(1, 101) if value%2 ==0] 
print(evens_list_zip)