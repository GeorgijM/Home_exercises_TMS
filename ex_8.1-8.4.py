# Задание 8.1

class Soda:

    def __init__(self, flavor=''):
        self.flavor = flavor

    def print_flavor(self):
        if len(self.flavor) > 0:
            print(f'You have {self.flavor} soda')
        else:
            print(f'Simple soda')


soda_1 = Soda("orange")
soda_2 = Soda('berry')
soda_3 = Soda()

soda_1.print_flavor()
soda_2.print_flavor()
soda_3.print_flavor()


# Задание 8.2
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)

    def subtraction(self):
        print(self.a - self.b)


x = Math(1, 2)
x.addition()
x.multiplication()
x.division()
x.subtraction()


# Задание 8.3
class Car:
    def __init__(self, color='', type='', year=''):
        self.color = color
        self.type = type
        self.year = year

    def engine_start(self):
        print('The car is started')

    def engine_off(self):
        print('The car is turned off')

    def car_year(self):
        self.year = input('Set the car year: ')
        print(f'The setted car year is {car_1.year}')

    def car_type(self):
        self.type = input('Set the car type: ')
        print(f'The setted car type is {car_1.type}')

    def car_color(self):
        self.color = input('Set the car color: ')
        print(f'The setted car color is {car_1.color}')


car_1 = Car()
car_1.engine_start()


# car_1.engine_off()
# car_1.car_year()
# car_1.car_type()
# car_1.car_color()


# Задание 8.4
class Sphere:
    def __init__(self, radius=1, x=0, y=0, z=0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return 4 / 3 * 3.141592 * self.radius ** 3

    def get_square(self):
        return 4 * 3.141592 * self.radius ** 2

    def get_radius(self):
        return self.radius

    def get_center(self):
        center = (self.x, self.y, self.z)
        return center

    def set_radius(self, r):
        self.radius = r
        print(f'The setted sphere radius is {r}')

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        print(f'The setted sphere center is {x, y, z}')

    def is_point_inside(self, x_inside, y_inside, z_inside):
        # return ((x_inside - self.x)**2 -(y_inside - self.y)**2 - (z_inside - self.z)**2) < self.radius ** 2
        return ((x_inside - self.x) ** 2 + (y_inside - self.y) ** 2 + (z_inside - self.z) ** 2) < self.radius ** 2


sphere_1 = Sphere()

print(sphere_1.get_volume())
print(sphere_1.get_square())
print(sphere_1.get_radius())
print(sphere_1.get_center())

sphere_1.set_radius(2)
sphere_1.set_center(0, 0, 0)

print(sphere_1.is_point_inside(1, 1, 1))
print(sphere_1.is_point_inside(3, 0, 0))

