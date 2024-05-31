class Vehicle:
    def __init__(self, make: str, miles: int, price: int):
        self.make = make
        self.miles = miles
        self.price = price
        self.engine_on = False

    def start_engine(self):
        print('Starting engine...')
        self.engine_on = True

    def make_noise(self):
        print('Beep beep!')

    def get_info(self):
        return f'The {self.make} has {self.miles} miles and costs ${self.price}.'


class Truck(Vehicle):

    def __init__(self, make: str, miles: int, price: int):
        super().__init__(make, miles, price)
        self.cargo = False

    def load_cargo(self):
        print('Loading the truck bed...')
        self.cargo = True

    def get_info(self):
        return f'The {self.make} truck has {self.miles} miles and costs ${self.price}.'


class Motorcycle(Vehicle):
    def __init__(self, make: str, miles: int, price: int, top_speed: int):
        super().__init__(make, miles, price)
        self.top_speed = top_speed

    def make_noise(self):
        print('Vroom vroom!')

    def get_info(self):
        return f'The {self.make} motorcycle has {self.miles} miles and costs ${self.price} and has a top speed of {self.top_speed}mph'
