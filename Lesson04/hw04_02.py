"""
Создайте абстрактный класс «Оргтехника», который будет базовым для классов - наследников. Эти классы — конкретные
типы оргтехники(принтер, сканер, ксерокс).В базовом классе определите абстрактные методы, общие приведённых
типов.В классах - наследниках реализуйте их, а также добавьте уникальные для каждого типа оргтехники функциональные
возможности.

Также создайте класс «Склад», экземпляр которого будет способен принимать в себя объекты техники на хранение.
Организуйте для него протокол итерации(чтобы объекты вашего склада можно было бы перебирать). """


from abc import ABC, abstractmethod


class Equipments(ABC):
    @abstractmethod
    def sale_on(self):
        pass

    @abstractmethod
    def sale_off(self):
        pass

    @abstractmethod
    def state(self):
        pass


class Notebook(Equipments):
    def __init__(self, vendor, model, serial_number, is_state):
        self.model = model
        self.serial = serial_number
        self.vendor = vendor
        self.is_sales = False
        self.is_state = is_state

    def sale_on(self):
        self.is_sales = True
        print('Продано')

    def sale_off(self):
        self.is_sales = False
        print('На складе')

    def state(self):
        if self.is_state == 'New':
            return f'Новый'
        return f'б/у'

    def __str__(self):
        return f"NoteBook {self.vendor}\nМодель {self.model}\ns/n {self.serial}\nСостояние {self.state()}"


class Stockroom:
    def __init__(self, name):
        self.name = name
        self.to_stockroom = []

    def add_to_stockroom(self, equipment):
        self.to_stockroom.append(equipment)

    def __iter__(self):
        return iter(self.to_stockroom)


n = Notebook('Asus', 'N700', 'QW2345', 'New')
n1 = Notebook('Sony','i100', '3r34t43', 'б/у')

print(n)
n.sale_on()

stock = Stockroom('Мой склад')
stock.add_to_stockroom(n)
stock.add_to_stockroom(n1)
for equipment in stock:
    print(equipment)



