import math
cat1 = float(input("Введите первый катет: "))
cat2 = float(input("Введите второй катет: "))
hypotenuse = math.sqrt(cat1**2 + cat2**2)
print("Гипотенуза равна", hypotenuse)