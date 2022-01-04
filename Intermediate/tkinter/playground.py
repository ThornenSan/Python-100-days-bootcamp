# Unlimited arguments
def add(*args):
    n_sum = 0
    print("arguments: ", args)
    print(type(args))
    for n in args:
        n_sum += n
    return n_sum


# print(add(3, 5, 6, 7, 8, 9, 10))


# Unlimited keyword arguments
def calculate(n, **kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


# my_car = Car(make="Nisan", model="GT-R")
my_car = Car(make="Nisan")
print(my_car.model)
