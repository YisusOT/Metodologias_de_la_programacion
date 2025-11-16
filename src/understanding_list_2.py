# Slicing (obtener pedazos de una lista)
players = ["cr7", "meesi", "Travis", "Hittler", "chicharito",]
print(players)
print(f"\n {players[0:3]}")
# Slice es trabajar con un grupo especifico de la lista "print(variable[(posicion cero):(posicion final -1)])"
print(f"\n {players[:4]}")
print(f"\n {players[2:]}")
print(f"\n {players[-3:-1]}")
print(f"\n The first tree players are {players[0:3]}")

students = ["axel", "Ignacio", "Jorge"]
for student in students[0:3]:
    print(student)

# Como copiar una lista

food = ['Pizza', 'gorditas de jaumave', 'machacado']
# copy_of_food = food # Manera incorrecta de copiar una lista
copy_of_food_1 = food[:]  # Manera correcta
copy_of_food_2 = food.copy()
copy_of_food_3 = list(food)

# Modificacion de elementos

cars = ["bwm", 'porch', 'masda', 'totoya', 'ford']
cars[0]= "bmw"
cars[1]= "porshe"
cars[2]= "mazda"
cars[3]= "toyota"
cars[0:4] = ("a", "b", "c", "d")
print(cars)