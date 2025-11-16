"""
Las tuplas son listas de elementos que no pueden cambiar su tamaño. las tuplas son listas inmutables

Se utilizan las () para definir una tupla

Ejemplo:
"""
# rectangulo (largo, ancho)
rectangule_dimensions = (200, 50) # Esto es una tupla
print(f"largo {rectangule_dimensions[0]} mm")  # = largo 200 mm
print(f"Ancho {rectangule_dimensions[1]} mm")  # = Ancho 50 mm

# Modificar una tupla
# rectangule_dimensions[0] = "20"  # = type_error, no se puede modificar una tupla

for dimension in rectangule_dimensions:
    print(dimension)

"""
No podemos modificar una tupla, ni agregar o eliminar elementos, lo que si podemos es cambiar la asignacion a una 
variable que almacena una tupla.
"""