## String
- Rust has two types to represent strings:
    - String : Modifiable, owned string
    - &str : A read-only String. String literal has this type. So basically the default when a string is saved in a variable.
- Both type of string always stores UTF-8 encoded strings.
- Raw string: `r#"the actual raw string with disabled escape like:\n"#;`
- Creating a variable with `String` type, there are many ways but the simples is to 
    - use `::new()` constructor.
    - Then push whatever we want to save as string.
    - `let mut sentence = String::new();`
    - `sentence.push_str("Hello,  world!"); `
- NOTE:
    - Since each character is of 4bytes, indexing a string with byte position might not always work
    as the byte poisition may not end  on a character boundry.
    - So it's better to use iterator than trying to index by  position.
    - The commented out line shows the same example where it does not end at boundry.

```rust
fn main() {
    let greeting: &str = "Greetings";
    let planet: &str = "🪐";
    let mut sentence = String::new();
    sentence.push_str(greeting);
    sentence.push_str(", ");
    sentence.push_str(planet);
    println!("final sentence: {}", sentence);
    println!("{:?}", &sentence[0..5]);
    //println!("{:?}", &sentence[12..13]);
    println!(r#"<a href="link.html">link</a>"#);
}
```
