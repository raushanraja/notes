from abc import ABC, abstractmethod


# Product
class Animal(ABC):

    @abstractmethod
    def speak(self):
        raise NotImplemented()


# Concrete Product One
class Dog(Animal):

    def speak(self):
        return "Woof!"


# Concrete Product Two
class Cat(Animal):

    def speak(self):
        return "Meow!"


# Creator
class AnimalFactory(ABC):

    # factory_method
    @abstractmethod
    def create_animal(self) -> Animal:
        raise NotImplemented()


# Concrete Create One
class DogFactory(AnimalFactory):

    def create_animal(self) -> Animal:
        return Dog()


# Concrete Create One
class CatFactory(AnimalFactory):

    def create_animal(self) -> Animal:
        return Cat()


# Client code
def main():
    factory = DogFactory()
    animal = factory.create_animal()
    print(animal.speak())

    factory = CatFactory()
    animal = factory.create_animal()
    print(animal.speak())


if __name__ == "__main__":
    main()

'''
The Factory Method is a creational design pattern in software engineering that 
provides an interface for creating objects 
but allows subclasses to alter the type of objects that will be created. 

Breakdown of above statement


1. Interface for Creating Objects: 
    - The interface for creating objects is defined by the AnimalFactory abstract class. (i.e, Creator)
    - This class has an abstract method create_animal(), which serves as the factory method. 
    - It declares the interface for creating Animal objects, but it does not specify the exact type of object to be created. 
    - This abstract method will be implemented by concrete subclasses (DogFactory and CatFactory) to create specific types of Animal objects.

2. Allows Subclasses to Alter the Type of Objects Created: 
    - Subclasses (DogFactory and CatFactory) extend the AnimalFactory class and provide their own implementations of the create_animal() method. 
    - Each subclass decides and specifies the type of Animal object to create. 
    - For example, DogFactory creates Dog objects, and CatFactory creates Cat objects. 
    - This is where the flexibility of altering the type of objects occurs. 
    - You can easily add new factories to create different types of animals without modifying the client code.
'''
