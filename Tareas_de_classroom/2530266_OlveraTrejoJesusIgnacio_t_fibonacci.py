"""
Jesus Ignacio Olvera Trejo

Grupo IM 1-2

Matricula: 2530266

Trabajo: Serie de Fibonacci
    La serie de Fibonacci es una secuencia infinita de números donde cada término es la suma de los dos anteriores, 
    comenzando usualmente con 0 y 1 (o 1 y 1). La secuencia se genera sumando los dos números previos: 
        0,1,1(0+1),2(1+1),3(1+2),5(2+3),8(3+5),
     y así sucesivamente.

    Para este trabajo, el usuario dara un numero que representa la posicion del numero en la serie, por ello debemos usar
    un algoritmo que pueda usar n numeros para n terminos, en otras palabras, que se pueda escoger cualquier numero natural
    entero hasta infinito y que aun asi el algoritmo arroje un resultado
"""
# verdadero codigo:
try:
  x = 0
  numbers = [0, 1]
  posicion = int(input('what posicion do you want?'))
  for coor in range(1, posicion-1):
    n = numbers[-1] + numbers[-2]
    numbers.append(n)
  for number in numbers:
    x = x + 1
    print(f'{x}.- {number}')
except:
  print('Set real numbers')

"""
Entradas:
  posicion: int

Salidas:
  serie_fibonacci: list

Validaciones:
- Verificar que posicion pueda convertirse a int.
- posicion >= 1; si no se cumple, mostrar "Error: invalid input".

Casos:
  what posicion do you want? 7
  1.- 0
  2.- 1 
  3.- 1
  4.- 2
  5.- 3
  6.- 5
  7.- 8

  what posicion do you want? a
  Set real numbers

  what posicion do you want? -3
  Set real numbers
"""
"""
Conclusion:
  En conclusion, este algoritmo permite calcular la serie de Fibonacci para cualquier posicion dada por el usuario, 
  siempre y cuando sea un numero natural entero. Mejore mi razonamiento logico y mi capacidad de descomponer
  problemas en pasos mas pequeños, ya que al principio me costo trabajo entender como funcionaba la serie y como podia
  implementarla en codigo y al principio use la proporcion aurea, cosa que no era necesaria para este problema y me 
  daba un resultado incorrecto para posiciones grandes por el redondeo de decimales.

Fuentes:
https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci
https://www.programiz.com/python-programming/examples/fibonacci-sequence
https://www.educ.ar/recursos/132013/la-matematica-incrustada-en-la-inmensa-variedad-de-formas-de-vida
https://www.eade.es/blog/186-la-sucesion-de-fibonacci-en-el-diseno
https://builtin.com/data-science/fibonacci-sequence
"""