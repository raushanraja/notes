### Tuple & Array
- Tuple and Array are compound types that can store a list of  data under same  variable.
- All the elements of array are of same type.
- All the elements of tuple can be of different type.
- Both types have a size fixed at compile time.
- Array def:  let arrayName [T;N]
- Tuple def; let tupleName (),(T,), (T1,T2), ... based on requirement.
```rust
// Array Assighment and access
fn main(){
    let mut numbers: [i8, 10] = [42;10]; // This initilizes all the 10 values as 42
    let mut twoDitigs: [i8, 2] = [1,2];

    println!('First number: {}', numbers[0]);
    println!('First digit: {}', twoDigits[0]);
}
```

```rust
// Tuple Assighment and access
fn main(){
    let mut values: ( i8, bool ) = (7,true); // This initilizes all the 10 values as 42

    println!('Value One: {}', values.0);
    println!('Value Two: {}', values.1);
}

```

### Array Iteration:
- `for` loop

### Pattern Matching
- Using `match` keyword. 
- The comarision are done from top to bottom.
- The structure looks something simiar to c/c++ switch statement.
- `_` pattern is used to match wildcard as matches all the remaining case.
- Some other chars used while  matching:
    - `|` as or
    - `..` to expand
    - `1..=5` to define a range
    - `_` as wildcard

### Destructuring
- Destructuring is way of extracting a part of data from a data structure.
- This destructuring pattern then can be used in pattern matching, variable binding etc.
- Using destructuring with array and tuple

```rust
// Destructuring with tuple
fn describe_point(point: (i32, i32)){
    match point {
        (0, _) => println!("On Y axis");
        (_, 0) => println!("On X axis");
        (x, _) if x < 0 => println!("left of Y axis");
        (_, y) if y < 0 => println!("below X axis");
        _ => println!("first quadrant");
    }
}

fn main(){
    describe_point(1,0);
}
```

```rust
// Destructuring with array
fn main() {
    let triple = [0, -2, 3];
    println!("Tell me about {triple:?}");
    match triple {
        [0, y, z] => println!("First is 0, y = {y}, and z = {z}"),
        [1, ..]   => println!("First is 1 and the rest were ignored"),
        [.., x]   => println!("Except last everything were ignored x={x}"),
        [a@.., z]   => println!("everything in a, last in z={z}"),
        _         => println!("All elements were ignored"),
    }
}
```
