"""
Напишите программу с классом Math. При инициализации
атрибутов нет. Реализовать методы addition, subtraction,
multiplication и division. При передаче в методы двух числовых
параметров нужно производить с параметрами
соответствующие действия и печатать ответ.
"""

class Math:
    # Сложение
    @staticmethod
    def addition(a, b):
        """Сложение двух чисел."""
        return a + b

    # Вычитание
    @staticmethod
    def subtraction(a, b):
        """Вычитание второго числа из первого."""
        return a - b

    # Умножение
    @staticmethod
    def multiplication(a, b):
        """Умножение двух чисел."""
        return a * b

    # Деление
    @staticmethod
    def division(a, b):
        """Деление первого числа на второе."""
        if b != 0:
            return a / b
        else:
            return "Ошибка: деление на ноль!"


# Пример использования:
math_instance = Math()
print("Сумма:", math_instance.addition(5, 3))
print("Разность:", math_instance.subtraction(10, 4))
print("Произведение:", math_instance.multiplication(2, 6))
print("Частное:", math_instance.division(8, 2))
