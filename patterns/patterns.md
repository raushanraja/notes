#### Design Patterns:
- Design patterns are reusable solution to common software design problems.
- These provide an efficient and maintainable way to solve problems.


#### Most common Design Patterns in python
- Creational Patterns
- Structural Patterns
- Behavioural Patterns
- Concurrency Patterns
- Idiomatic Patterns


#### Creational Patterns
- These patterns are related to object creational mechanisms.
- Trying to create objects in a suitalbe manner to the situation.
- Most common creational patterns:
    - Factory Method
    - Abstract Factory
    - Builder
    - Prototype
    - Singleton


#### Structural Patterns
- These patterns focuses on organizing and composing objects and form larger structure.
- Most common Structural Patterns:
    - Composite
    - Adapter
    - Bridge
    - Decorator
    - Facade
    - Proxy
    - Flyweight


#### Behavioural Patterns
- These patterns address how 
    - Object/classes communicate & collabrate with each other and
    - Assignment of responsibilites between objects
- This pattern deals with algorithms rather than the structure of the code
- Most common Behavioural Patterns:
    - Observer 
    - Strategy
    - Command
    - State
    - Chain of Responsibility
    - Interpreter
    - Iterator
    - Mediator
    - Memento 
    - Visitor
    - Template Method


#### Concurrency Patterns
- These pattern address challanges of
    - design and managing concurrent and parallel execution
    in multi-threaded or destributed system
- This pattern helps in ensuring that
    - Thread or Process work together efficiently and safely
    - Avoid issues like race-condition and resource contention
- Helps in designing reliabl, responsive and scalable systems
- Most common Concurrency Patterns:
    - Producer-Consumer pattern
    - Semaphore 
    - Mutex (Mutual Exclusion)
    - Read-Write Lock 
    - Thread Pool
    - Future & Promise
    - Barrier
    - Actor Model


#### Idiomatic Patterns
- Idiomatic : Confirming to customary way of doing things.
- Idiomatic Patterns are
    - established conventions and best practices in a specific programming language or framework. 
- These represents most natural, readable, consistent and efficient way to do things.
- Example:
    - Python's list comprehension
    - Naming conventions for codes in a specific language
    - Using map/filter in javascript


##### Factory Method
- This patterns provides a way to create objects without specifying the exact class of object.
- It defines a factory method which subclass can override to specify the class of object they create.
- ```python
    
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

  ```

##### Abstract Factory
- 



