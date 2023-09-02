class Car:
    def __init__(self, make, model):
        self._make = make
        self._model = model
        self._body = 'small'

    def __str__(self):
        return f'Car: {self._make} {self._model}, body type: {self._body}'


class Truck:
    def __init__(self, make, model):
        self._make = make
        self._model = model
        self._body = 'large'

    def __str__(self):
        return f'Truck: {self._make} {self._model}, body type: {self._body}'


# Factory Method
def Factory(make, model, veh_type):
    vehicals = {
        'car': Car,
        'truck': Truck
    }
    return vehicals[veh_type.lower()](make, model)


class FactoryClass:
    _vehicals_dict = {
        'car': Car,
        'truck': Truck
    }

    def __init__(self):
        self._vehicals = []

    def create_vehicals(self, make, model, veh_type):
        vehical = self._vehicals_dict[veh_type.lower()](make, model)
        self._vehicals.append(vehical)
        return vehical


if __name__ == "__main__":

    print('\nFactory Method:')
    car1 = Factory('Honda', 'Civic', 'car')
    truck1 = Factory('Toyota', 'Tundra', 'truck')

    print(car1)
    print(truck1)


    print("\nFactory Class:")
    factory = FactoryClass()
    factory.create_vehicals('Honda', 'Civic', 'car')
    factory.create_vehicals('Toyota', 'Tundra', 'truck')

    print(car1)
    print(truck1)
