## Structs
- Stuct is a composite data type.
- Which allows to group variables of different type together.
- Each elements within a struct is called a `field`.
- Different type of struct:
    - Named Struct
    - Tuple Struct
    - Unit Struct
    - Struct with Generics


### Named Structs
- Struct allows to define custom tupes similar to C/C++.
- With Rust Struct there is no concept of inheritance between structs.
- Named Struct is one of the Struct type where each field can have a name. 
- In Named struct, field name can be used as shorthand to initialize it.
- `..StructName` syntax can be used to copy the remaining field from old to new struct.

```rust
struct Person {
    name: String,
    age: u8,
}

fn describe(person: &Person){
    println!("{} is {} years old", person.name, person.age);
}

fn main(){
    let mut peter = Person{
        name: String::from("Pan"),
        age: 34
    };

    describe(&peter);
    peter.age = 22;
    describe(&peter);

    let name = String::from("Peter");
    let age = 32;

    // Field names shorthand to initialize the struct
    let pan = Person{name, age};

    describe(&pan);

    // `..StructName` syntax to copy the fields from one to another struct
    let john = Person{name: String::from("John"), ..pan};
    describe(&john);
}
```

### Tuple Struct
- A Tuple struct is way to define a struct without field names.
- It is useful for single field wrapper call `newtypes`
- The fields are accessed via index.
```rust

// Tuple Struct
struct Point(i32, i32);

fn main(){
    let pointOne = Point{10,20};
    println!("Values are : {}, {}", pointOne.0, pointOne.1);
}


```

```rust
// A newtype, where we encode some additional information about value in primitive type
// For example: We can create a variables of type PhnoeNumber Struct after verifying the data
// And When we use this variables anywhere we do not need to varify it again
struct PhnoeNumber(String);
```

### Unit Struct
- A struct with no field is called Unit Struct.
- This is used when there is a need of a Type without any data. 
- It is possible to define method for unit struct. 
```rust
struct Greeter;

impl Greeter{
    fn greet(&self){
        println!("Hello!");
    }
}

fn main(){
    let greeter = Greeter;
    greeter.greet();
}
```
