#### Flyweight Pattern:
- It is a structural design pattern.
- It helps in to optimizing memory usage by sharing common parts.
- To accomplish this
    - It's suggested to store only Intrinsic state in Flyweight object.
- The object that stores only Intrinsic state is called Flyweight.

##### Intrinsic State:
- The constant data of an object is usually called Intrinsic state.
- These state lives within the objects.
- Other objects can read the state, but cannot change it.

##### Extrensic State:
- The states that can be altered from outside by other objects.

##### Steps to implement flyweight pattern:
- Create a Flyweight Class (Contains only Intrinsic state) 
- Add methods with Extrensic States as method parameter
- Create a Factory Class to manage pool of flyweights
    - with cache and Intrinsic state as cache's key
- Move Extrensic state and flyweight reference to a seperate context class. 
- Use the Flyweight in Client class. 
