class Car:
    def _init_(self, make, model):
        self.public_make = make # Открытый атрибут
        self ._protected_model = model # Защищенный атрибут
        self .__private_year = 2022 # Приватный атрибут

    def public_method(self):
        return f"Это открытый метод. Машина: {self.public_make} {self._protected_model}."

    def _protected_method(self):
        return "Это защищенный метод."

    def __private_method(self):
        return "Это приватный метод."

class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super()._init_(make, model)
        self.battery_size = battery_size

    def get_details(self):
        # Можно обратиться к открытому и защиценному атрибуту, но не к приватному
        details = f"{self.public_make}, {self ._protected_model}, Батарея: {self.battery_size} kWh."
        # Нельзя напряную обратиться к __ private_method и __ private_year
        return details

# создание ел машины
tesla = ElectricCar("Tesla","Model S",100)

# Доступ к открытому атрибуту и методу:
print(tesla.public_make)
print(tesla.public_method())

# Доступ к защищённому атрибуту (не рекомендуется, но возможно):
print(tesla._protected_model)
print(tesla._protected_method())

print(tesla._Car__private_year)