# understanding_looping.py

magicians = ["ron", "harry", "snape", "hermione"]

for magician in magicians:
    print(magician) # Correctly iterating through the list and printing each magician's name
    print(magician.upper()) # Printing the name in uppercase
    print(f"{magician.title()} ese fue un gran hechizo.") # Using f-string to format the output
    print("\n") # Adding a newline for better readability

print("Gracias a todos los magos por participar en el espectáculo.") # Final message after the loop


"""
    Python utiliza la identacion para determinar
    cuando una linea dee codigo esta conectada
    a la linea de codigo anterior.

    Basicamente, se utiliza 4 espacios para cada nivel de identacion, 
    para obligarnos a escribir codigo limpio y legible.

    Identacion correcta:
    El bloque de código dentro del bucle for está correctamente indentado.

    Debe de estar alineado con el for para que se ejecute en cada iteración del bucle.

    Identación incorrecta:


    El print final no está indentado correctamente.
    Por lo tanto, se ejecutará solo una vez después de que el bucle haya terminado,

   """

 # No olvidemos identar (donde se necesita y no identar donde no se necesita.)
# Ejemplo:
magicians = ["alice", "david", "jorge", "candelario"]

for magician in magicians:
    #Esto causará un error de indentación
    #print(magician)  #Solucion: identar esta línea para que esté dentro del bucle


#Ejemplo correcto:
 magicians = ["alice", "david", "jorge", "candelario"]
for magician in magicians:
    print(magician)  # Correctamente indentado dentro del bucle
    print(f"Great{magician},! I can't wait to see your next trick.\n")

#Ejemplo incorrecto:
#print(f"Great {magician}!, I can't wait to see your next trick.\n")

# Identacion inecesaria:
messsage = "Hello Charly!"
 #print(messsage) Esto causará un error de indentación

#Identacion correcta:
message = "Hello Charly!"
print(message)  # Correctamente alineado al margen izquierdo
    

# Logical error con indentacion:

magicians = ["alice", "david", "jorge", "candelario"]
for magician in magicians:
    print(magician)
    print(f"Great {magician}!, I can't wait to see your next trick.\n")
    #print("Thank you everyone, that was a great magic show!") identacion incorrecta
    # Solucion: identar esta línea para que esté fuera del bucle
print("Thank you everyone, that was a great magic show!")  # Correctamente alineado al margen izquierdo 

# Logical sintaxtix
magicians = ["alice", "david", "jorge", "candelario"]
for magician in magicians
 # Error de sintaxis: falta dos puntos al final de la línea
 #Nota: el error esta puesto aproposito para fines educativos Ignacio
    print(magician)
    print(f"Great {magician}!, I can't wait to see your next trick.\n")

# Solucion:
magicians = ["alice", "david", "jorge", "candelario"]
for magician in magicians:
    print(magician)
   