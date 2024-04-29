class Calculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2

def main():
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        operation = input("Выберите операцию (+, -, /, *): ")

        calculator = Calculator()

        if operation == "+":
            result = calculator.add(num1, num2)
        elif operation == "-":
            result = calculator.subtract(num1, num2)
        elif operation == "*":
            result = calculator.multiply(num1, num2)
        elif operation == "/":
            result = calculator.divide(num1, num2)
        else:
            print("Недопустимая операция. Пожалуйста, выберите из +, -, /, *.")
            return

        print(f"Результат: {result:.2f}")
    except ValueError:
        print("Пожалуйста, введите корректные числа.")

if __name__ == "__main__":
    main()
