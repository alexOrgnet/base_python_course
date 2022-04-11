"""
1. Создать класс TrafficLight (светофор).
#определить у него один атрибут color (цвет) и метод running (запуск);
#атрибут реализовать как приватный;
#в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
#продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
#переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
#проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self, times, red, yellow, green):
        i = 0
        while i != times:
            ii = 0
            while ii != 3:
                if ii == 0:
                    sleep(red)
                elif ii == 1:
                    sleep(yellow)
                elif ii == 2:
                    sleep(green)
                print(TrafficLight.__color[ii])
                ii += 1
            i += 1


t = TrafficLight()
t.running(3, 7, 2, 1)

"""
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
проверить работу метода.

"""

class Road:

    def __init__(self, length, width):
        self._width = width
        self._length = length
        self.height = 5
        self.weight = 25

    def mass_asphalt(self):
        mass = self._length * self._width * self.weight * self.height / 1000
        print(
            f'Для покрытия всего дорожного полотна длиной {round(self._length)} м. и шириной {round(self._width)} м. необходимо {round(mass)} кг асфальта')


r = Road(1000, 10)
r.mass_asphalt()


"""
3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name+" "+self.surname

    def get_total_income(self):
        return self._income["wage"]+self._income["bonus"]


position = Position('Ivan', 'Ivanovich', 'Driver', '100000', '20000')

print(position.get_full_name(), position.get_total_income())

"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""

class Car:

    def __init__(self, name, speed, color, police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.police = police

    def go(self):
        return f'The {self.name} went.'

    def stop(self):
        return f'\nThe {self.name} has stopped.'

    def turn(self, direction):
        return f'\nThe {self.name} turned {direction}'

    def indicate_speed(self):
        return f'\nYour speed is {self.speed}'


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


class WorkCar(Car):

    def __init__(self, speed, color, name, police):
        super().__init__(speed, color, name, police)

    def indicate_speed(self):
        if self.speed > 40:
            return f'\nYour speed is higher than speed allowed! The speed of car {self.name} is {self.speed}'
        else:
            return f'The speed of car {self.name} is ok'


class TownCar(Car):
    def indicate_speed(self):
        if int(self.speed) > 60:
            return f'\nYour speed is higher than allow! Your speed is {self.speed}'
        else:
            return f'Speed of {self.name} is normal'


workCar = WorkCar('UAZ', 50, 'blue', False)

print('1:\n' + workCar.go(), workCar.indicate_speed(), workCar.turn('left'), workCar.stop())

townCar = TownCar('Ford', 60, 'white', False)

print('2:\n' + townCar.go(), townCar.indicate_speed(), townCar.turn('left'), townCar.stop())

sportCar = SportCar('AudiRS', 170, 'red', False)
print('3:\n' + sportCar.go(), sportCar.indicate_speed(), sportCar.turn('right'), sportCar.stop())

policeCar = PoliceCar('Kia', 100, 'yellow', True)
print('4:\n' + policeCar.go(), policeCar.indicate_speed(), policeCar.turn('left'), policeCar.stop())


"""
5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'\nЗапуск отрисовки')


class Pen:

    def __init__(self):
        pass

    def draw(self):
        print(f'\nЗапуск отрисовки ручкой')


class Pencil:

    def __init__(self):
        pass

    def draw(self):
        print(f'\nЗапуск отрисовки карандашом')


class Handle:

    def draw(self):
        print(f'\nЗапуск отрисовки маркером')


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
