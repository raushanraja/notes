## Static & Const
- Static and const variable are two different ways to create globally-scoped values.
- These values cannot be mover or reallocated during the execution of the program.

### Const
- Const variable are evaluated at compile time.
- Their value are inlined whenever they are used.
- Only functions marked `const` can be called at runtime to generate a `const` value.
- Other `const` functions can be called at runtime.
```rust
const DIGEST_SIZE: usize = 3;
const ZERO: Option<u8> = Some(42);

fn compute_digest(text: &str) -> [u8; DIGEST_SIZE] {
    let mut digest = [ZERO.unwrap_or(0); DIGEST_SIZE];
    for (idx, &b) in text.as_bytes().iter().enumerate() {
        digest[idx % DIGEST_SIZE] = digest[idx % DIGEST_SIZE].wrapping_add(b);
    }
    digest
}

fn main() {
    let digest = compute_digest("Hello");
    println!("digest: {digest:?}");
}
```

### Static
- Static variables will live during the whole execution of the program.
- This cannot be moved.
- Static provides object identity (An address in memory & state)
```rust
static Banner: &str = "Welcom to Rust";

fn main(){
    println!("{BANNER}");
}
```
