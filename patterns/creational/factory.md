### Factory Pattern
- It's a part of creational design pattern.
- Factory Pattern provides a way to create an object without specifying exact class.
- Variants of Factory Pattern
    1. Factory Method
    2. Abstract Factory
    3. Factory Class

#### 1. Factory Method
- Factory Method provides an Interface for creating objects.
- But Interface does not actually creates the object but allows subclasses to alter the type of object to create.
- Main Components of Factory Methods:
    - Creator : The Abstract Class that provides the Interface with factory_method.
    - ConcreteCreator : Subclasses that provides actuall implementation of factory_method and return a specific object from ConcreteProduct.
    - Product : This is an abstract class,  provides common Interface for all prouduct created by factory_method, and used by Creator & ConcreteCreator.
    - ConcreteProduct : These are classes that implements Product Interface, and represents an actual object created by factory_method.
- Steps:
    - Create an interface for the objects we want (Product)
    - Provide implementation for the Interface (ConcereteProduct)
    - Create an interface with factory method (Creator)
    - Provide implementation for the above interface for each type of object (ConcreteCreator)

