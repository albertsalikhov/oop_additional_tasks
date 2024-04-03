"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Важно в конструкторе обрабатывать исключения, если год больше текущего
"""
import datetime




class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        if year > datetime.date.today().year:
            raise Exception('Эта машина еще не была выпущена')
        self.year = year





# код для проверки
car = Car('Toyota', 'Corolla', 2022)
print(car.brand)
print(car.model)
print(car.year)

# car2 = Car('Toyota', 'Corolla', 3000)
# raises Exception('Эта машина еще не была выпущена')
