class Soda:
    def __init__(self, flavor=None):
        self.flavor = flavor

    def __str__(self):
        if self.flavor:
            return f"У вас газировка с {self.flavor} вкусом"
        else:
            return "У вас обычная газировка"

# Пример использования:
soda1 = Soda("клубничный")
print(soda1)  # Выведет: "У вас газировка с клубничным вкусом"

soda2 = Soda()
print(soda2)  # Выведет: "У вас обычная газировка"
