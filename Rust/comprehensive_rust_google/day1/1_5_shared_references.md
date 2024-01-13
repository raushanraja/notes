### References
- A reference is a way to access another value without taking responsibility for it.
- This is similar to Pointers in c/c++, where reference contains the address of a variable.
- This way of taking a reference in rust of a value is called `borrowing`.
- A reference of type T has type &T.
- A reference can be created using `&` operator.
- It can be de-referenced (yeild it's value) by using `*` operator.

```rust
fn main() {
    let a = 'A';
    let b = 'B';

    // Creating a reference
    let mut r: &char = &a;

    // De-referencing the reference to get it's value
    println!("r: {}", *r);
    r = &b;

    // Updating the reference to point to the address of variable b
    println!("r: {}", *r);

    // Updating the value of reference
    // This won't work as we are tyring to update a Shared Reference
    // Even though the variable is mutable
    *r = 'C'
    println!("r: {}", *r);
}
```


### Shared Reference
- Shared reference is a read-only reference to a value.
- I.E, the value of a reference is immutalbe and cannot be modified. 


### Exclusive References
- AKA, Mutable Reference allows changing the value of the variable they refer to.
- These References has type `&mut T`

```rust
fn main() {
    let mut point = (1,2);
    println!("Point: {point:?}");

    // This is Mutable References
    let x_coord = &mut point.0;

    // changing the value of point.0
    *x_coord = 20;
    println!("Point: {point:?}");
}
```
