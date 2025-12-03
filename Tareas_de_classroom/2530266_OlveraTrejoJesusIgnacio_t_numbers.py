"""
Jesus Ignacio Olvera Trejo

Grupo IM 1-2

Matricula: 2530266

"""

# Problemas:
print('\n\n\nProbblema 1\n')
"""
 Problema 1: Convierte una temperatura en grados Celsius (float) a Fahrenheit y Kelvin. 
 Además, determina un valor booleano is_high_temperature que sea true si la temperatura 
 en Celsius es mayor o igual que 30.0 y false en caso contrario.

"""
try:
    temperature = float(input('Set the temperature in celsius: '))

    fahrenheit = (3*temperature*9/5) + 32 
    print(f"The temperature in fahrenheit is {fahrenheit}")
    kelvin = temperature + 273.15
    if kelvin >= 0:
      print(f"The temperature in kelvin is {kelvin}")
    else:
      print("the temperature in kelvin is below cero")
    if temperature >= 30:
        print('the temperature is high')
    else:
        print("the temperature is low")
except:
    print('set a real number')

""" 
Entradas:
  temperature


Salidas:
  farenheit
  kelvin
  boolean:
    True: hight_temperature
    False: low_temperature

Validaciones:
- Verificar que temp_c pueda convertirse a float.
- No permitir temperaturas físicas imposibles en Kelvin (por ejemplo, temp_k < 0.0).

Casos:
  Set the temperature in celsius: f
  set a real number

  Set the temperature in celsius: -32
  The temperature in fahrenheit is -140.8
  The temperature in kelvin is 241.14999999999998
  the temperature is low

  Set the temperature in celsius: 46
  The temperature in fahrenheit is 280.4
  The temperature in kelvin is 319.15
  the temperature is high
"""

## problema 2:
print('\n\n\nProblema 2\n')
"""
Calcula el pago total semanal de un trabajador. Hasta 40 horas se pagan a hourly_rate
(float). Las horas extra (> 40) se pagan al 150% de la tarifa normal. 
Además, genera un booleano has_overtime que indique si el trabajador hizo horas extra.
"""
try:
    work_time = int(input('How hours was you work this week? '))
    salary = 50
    if 0 <= work_time <= 40:
        pay = salary * work_time
        print(f"you worked {work_time} hours, then, you pay is {pay} dollars")
    elif work_time > 40:
        extra_work = work_time - 40
        pay_extra = extra_work*(salary*1.5)
        pay = salary*40
        print(f"you worked {work_time}") 
        print(f"your pay is {pay_extra + pay} dollars") 
        print(f"you worked {extra_work} hours extra")
    else:
      print('Set a real number')
except:
    print('Set a real number')

"""
Entradas:
  work_time

Salidas:
  pay
  extra_work
  extra_pay
  total_pay

Validaciones:
- hours_worked >= 0
- hourly_rate > 0
- Si alguno no cumple, mostrar "Error: invalid input".

Casos:
  How hours was you work this week? 45
  you worked 45
  your pay is 2375.0 dollars
  you worked 5 hours extra

  How hours was you work this week? -4
  Set a real number

  How hours was you work this week? 21
  you worked 21 hours, then, you pay is 1050 dollars
"""
## problema 3
print('\n\n\n Porblema 3\n')
"""
Determina si un cliente obtiene un descuento en su compra. La regla es:
- Tiene descuento si:
  - is_student es true OR
  - is_senior es true OR
  - purchase_total >= 1000.0
Calcula también el total a pagar aplicando un 10% de descuento cuando sea elegible.
"""
try:
    cost = int(input('How cost your shop? '))
    if cost >= 1000:
        final_cost = cost - (cost * 0.1)
        print(f"your final cost is {final_cost}")
    else:
        is_student = str(input("Are you a student? yes/no "))
        if is_student.lower() == 'yes':
            final_cost = cost - (cost * 0.1)
            print(f"your final cost is {final_cost}")
        else:
            is_senior = str(input("Are you a senior? yes/no "))
            if is_senior.lower() == 'yes':
                final_cost = cost - (cost * 0.1)
                print(f"your final cost is {final_cost}")
            else:
                print(f'your shop cost {cost}')
except:
    print('please, fill the questions correctly')

"""
Entradas:
  cost
  is_student
  is_senior

Salidas:
  final_cost

Validaciones:
- purchase_total >= 0.0
- Normalizar is_student_text e is_senior_text a mayúsculas y convertir a booleanos is_student, is_senior.
- Si el texto no es "YES" ni "NO", mostrar "Error: invalid input".

Casos:
  How cost your shop? 6678
  your final cost is 6010.2

  How cost your shop? 2
  Are you a student? yes/no yes
  your final cost is 1.8

  How cost your shop? 100
  Are you a student? yes/no no
  Are you a senior? yes/no yes
  your final cost is 90.0
"""

## Problema 4:
print('\n\n\n Problema 4: \n')
"""
Descripción:
Lee tres números enteros y calcula: suma, promedio (float), valor máximo, valor mínimo y 
un booleano all_even que indique si los tres números son pares.
"""
try:
  all_even = False
  num1= int(input('Set your first number '))
  num2= int(input('Set your second number '))
  num3= int(input('Set your third number '))
  suma = num1 + num2 + num3
  average = suma / 3
  list_of_numbers = []
  list_of_numbers.append(num1)
  list_of_numbers.append(num2)
  list_of_numbers.append(num3)
  list_of_numbers.sort(reverse=False)
  if num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2== 0:
    all_even = True
  if all_even:
    print('All numbers are even')
  else:
    print('Some number is odd')
  print(f'The sum of your numbers is {suma}')
  print(f'the average is {average}')
  print(f'The big number is {list_of_numbers[-1]}')
  print(f'The small number is {list_of_numbers[0]}')
except:
  print('Error in something')

"""
Entradas:
  num1
  num2
  num3

Salidas:
  all_even
  suma
  average
  big_number
  small_number

Validaciones:
- Verificar que los tres valores se puedan convertir a int.
- No se requieren restricciones adicionales (se permiten negativos).

Casos:
  Set your first number 2
  Set your second number 3
  Set your third number 4
  Some number is odd
  The sum of your numbers is 9
  the average is 3.0
  The big number is 4
  The small number is 2

  Set your first number 2
  Set your second number 4
  Set your third number 6
  All numbers are even
  The sum of your numbers is 12
  the average is 4.0
  The big number is 6

  Set your first number 1
  Set your second number 2
  Set your third number a
  Error in something
"""

# Problema 5:
print('\n\n\n Problema 5: \n')
"""
Descripción:
Determina si una persona es elegible para un préstamo con base en:
- monthly_income (float)
- monthly_debt (float)
- credit_score (int)
La regla es:
- debt_ratio = monthly_debt / monthly_income
- eligible es true si:
  - monthly_income >= 8000.0 AND
  - debt_ratio <= 0.4 AND
  - credit_score >= 650
"""
try:
  monthly_income = float(input('Set your monthly income: '))
  monthly_debt = float(input('Set your monthly debt: '))
  credit_score = int(input('Set your credit score: '))
  debt_ratio = monthly_debt / monthly_income
  candidate= 0
  if monthly_income >= 8000:
    candidate = candidate + 1
  else:
    print("You don't have good income")
  if debt_ratio <= 0.4:
    candidate = candidate + 1
  else:
    print("You don't have good debt radio")
  if credit_score >= 650:
    candidate = candidate + 1
  else:
    print("You haven't good credit score")

  if candidate == 3:
    print('You have all requirements, you gain the loan')
except:
  print('Set a real number')

"""
Entradas:
  monthly_income
  monthly_debt
  credit_score

salidas:
  candidate

Validaciones:
- monthly_income > 0.0 (evitar división entre cero).
- monthly_debt >= 0.0
- credit_score >= 0
- Si no se cumple, mostrar "Error: invalid input".

Casos:
  Set your monthly income: 2000
  Set your monthly debt: a
  Set a real number

  Set your monthly income: 2999
  Set your monthly debt: 200
  Set your credit score: 700
  You don't have good income

  Set your monthly income: 10000
  Set your monthly debt: 2
  Set your credit score: 40000
  You have all requirements, you gain the loan
"""

# Problema 6:
print('\n\n\n Problema 6: \n')
"""
Descripción:
Calcula el índice de masa corporal (BMI) de una persona con la fórmula:
- bmi = weight_kg / (height_m * height_m)
Además, genera booleanos para indicar:
- is_underweight (bmi < 18.5)
- is_normal (18.5 <= bmi < 25.0)
- is_overweight (bmi >= 25.0)

"""
try:
  weight = float(input('set your weight in kilograms: '))
  height = float(input('Set your height in meters: '))
  bmi = weight / (height * height)
  if weight > 0 and height>0:
    if bmi < 18.5:
      print(f'You are underweight, your bmi is {bmi}')
    elif bmi >= 18.5 and bmi < 25:
      print(f'You are normal, your bmi is {bmi}')
    elif bmi >= 25:
      print(f'You are overweight, your bmi is {bmi}')
  else:
    print('Set a real number')
except:
  print('Set only numbers')

"""
Entradas:
  weight
  height

Salidas
  bmi

Validaciones:
- weight_kg > 0.0
- height_m > 0.0
- Si no se cumple, mostrar "Error: invalid input".

Casos:
  set your weight in kilograms: 90
  Set your height in meters: 1.75
  You are overweight, your bmi is 29.387755102040817

  set your weight in kilograms: 50
  Set your height in meters: 1.58
  You are normal, your bmi is 20.028841531805796

  set your weight in kilograms: 3
  Set your height in meters: -2
  Set a real number
"""
"""
conclusion:
  En conclusion, este trabajo se me hizo mas facil que el de strip, 
  ya que las funciones de los numeros son muy intuitivos y no son tantos
  como los strings

Referencias:
https://www.altcademy.com/blog/how-to-multiply-in-python
https://docs.kanaries.net/es/topics/Python/
https://es.linkedin.com/advice/1/what-key-steps-converting-string-integer-python-f6naf?lang=es
https://www.datacamp.com/tutorial/how-to-convert-a-string-into-an-integer-in-python
https://www.freecodecamp.org/news/python-convert-string-to-int-how-to-cast-a-string-in-python
"""