### Abstract Factory Pattern
- It is creational design patter.
- It provides an interface for creating **families** or **dependent/related** objects
whithout specifying their concerete classes.
- It is a way to ensure that created objects are compatible together.
- Mostly used to situations where we need to create objects with:
    - Common themer or
    - Common set of properties
    - Example:
        - UI Component for different operating system (macOS, Linux, windows).
        - Database driver for different database management systems(Oracle, PostgreSQL, MySQL).

- Main Components:
    - Abstract Factory
        - Defines a set of creation method of creating various object.
    - Concerete Factories
        - These implemetns  Abstract Factory and provides implemetation for creating a family of object.
    - Abstract Products
        - Defines Interface for a product with common properties and behaviour.
    - Concerete Products
        - These implemetns Abstract Product and provides implemetation for a specific object.

