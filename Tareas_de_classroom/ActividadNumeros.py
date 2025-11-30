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
    convert = str(input('Can you convert to "farenheit" or "kelvin"? ' ))
    if convert == 'farenheit':
        fahrenheit = (3*temperature*9/5) + 32 
        print(fahrenheit)
    elif convert == "kelvin": 
        kelvin = temperature + 273.15
        print(kelvin)

    if temperature >= 30:
        print('the temperature is high')
    else:
        print("the temperature is low")

  
except:
    print('set a real number')

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
    if work_time <= 40:
        pay = salary * work_time
        print(f"you worked {work_time} hours, then, you pay is {pay} dollars")
    elif work_time > 40:
        extra_work = work_time - 40
        pay_extra = extra_work*(salary*1.5)
        pay = salary*40
        print(f"you worked {work_time}, then, your pay is {pay_extra + pay} dollars because you worked {extra_work} hours extra and this hours is 150% more")
except:
    print('Set a real number')

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

  if bmi < 18.5:
    print(f'You are underweight, your bmi is {bmi}')
  elif bmi >= 18.5 and bmi < 25:
    print(f'You are normal, your bmi is {bmi}')
  elif bmi >= 25:
    print(f'You are overweight, your bmi is {bmi}')
except:
  print('Set real numbers')