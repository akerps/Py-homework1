#Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x, y, z = int(input('Введите число x: ')), int(input('Введите число y: ')), (input('Введите число z: '))

left_value = not(x or y or z)
right_value = not x and not y and not z
result = left_value == right_value
if result == True:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")