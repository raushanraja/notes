## Enums
- Enums are craete of a type which has a different variants.
- Along with payload, Rust stores a descriminates. 
- Descriminates helps at runtime, to know which variant a variable is. 
- Normally Rust tries to use minimal space to store descriminates, but it can be changed.
```rust
#[derive(Debug)]
enum Direction{
    Left,
    Right
}
fn main(){
    let left: Direction = Direction::Left;
    println!("On this turn: {:?}", left);
}
```

```rust
//Custom Descriminates Example
#[repr(u32)]
enum Bar {
    A, // 0 , If we don't define. It starts with 0
    B = 10000, // We define it here and after this every new field increments it.
    C, // 10001, incremented automatically
}

fn main() {
    println!("A: {}", Bar::A as u32);
    println!("B: {}", Bar::B as u32);
    println!("C: {}", Bar::C as u32);
}
```
