class Car:
    speed = 0

    def __init__(self, color, name, is_police):
        self.color = color
        self.name = name
        self.is_police = is_police

    def go_car(self, speed):
        self.speed = speed
        return print('Авто поехала')

    def stop_car(self):
        self.speed = 0
        return print(f'Скорость авто {self.speed}, авто остановлен')

    def show_speed(self):
        return print(f'Текущая скорость {self.speed}')


car1 = Car("Red", "Lada", False)
car1.go_car(30)
car1.go_car(40)
car1.stop_car()
car1.show_speed()


