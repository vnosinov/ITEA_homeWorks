class Car:
    speed = 0
    direction = ''

    def __init__(self, color, name, is_police):
        self.color = color
        self.name = name
        self.is_police = is_police

    def go_car(self, speed):
        self.speed = speed
        return 'Авто поехала'

    def stop_car(self):
        self.speed = 0
        return f'Скорость авто {self.speed}, авто остановлен'

    def show_speed(self):
        return f'Текущая скорость {self.speed}'

    def turn_car(self, direction):
        self.direction = direction
        if self.speed != 0:
            return f'Машина едет {direction}'
        else:
            self.stop_car()


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Скорость вашего авто превышает 60 км/с, текущая скорость {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Скорость вашего авто превышает 40 км/с, текущая скорость {self.speed}')


class SportCar(Car):
    def show_speed(self):
        super().show_speed()
        print(f'У Вас СпортКар, гони сколько можешь, текущая скорость {self.speed}')


class PoliceCar(Car):
    def police_on_the_road(self):

        if not self.is_police:
            return
        print('Полиця на дороге всем принять в право')


if __name__ == "__main__":
    # car1 = Car("Red", "Lada", False)
    # car1.go_car(30)
    # car1.go_car(40)
    # car1.stop_car()
    # car1.show_speed()
    # car1.turn_car('на лево')
    car2 = TownCar('Зеленый', 'Nissan', False)
    car2.go_car(61)
    car2.show_speed()
    car3 = PoliceCar("Черно-Белый", "Toyota", False)
    car3.police_on_the_road()
