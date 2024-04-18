num1 = (input("Введите первое число: "))
num2 = (input("Введите второе число: "))

if not (num1.isdigit() and num2.isdigit()):
    print("Пожалуйста, введите числа!")
    exit()

num1 = float(num1)
num2 = float(num2)

operation = input("Выберите операцию (+ ,- ,/ ,* ) ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2

if operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2

print("Результат: ",result)
