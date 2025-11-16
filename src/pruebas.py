num = 0
num = int(input("Set your age  "))
lista = list(range(0, num))
for value in lista:
    print(value)

print('\n\n\n')
print("AÑO BICIESTO")
num = int(input("Set your year  "))

if num in range(1000, 9999):
    if num%4 == 0 and num%100 != 0:
        print("your year is biciesto")
    else:
        if num%100 == 0 and num % 400 == 0:
            print('your year is biciesto') 
        else:
            print('your year is NOT biciesto')
else:
    print('Error, number out of range')
