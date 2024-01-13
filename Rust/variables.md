### Variables: Lifetime, Reference, Borrow
- Variable Bindings have lifetime. I.E, they exists only in the block they are specified.
- Varaible References have a lifetime as well.
- And the lifetime of a `Variable Reference` cannot exceed the lifetime of a `Variable Binding` it borrows from.
- Example:
-
    ```rust
        // Vairable Binding Lifetime
        fn main(){
                // `x` does not exist yes
            {
                let x = 42;
                println!("X: {}", x);  // `x` starts existing
            }
            // `x` stops existing
        }
            // `x` no longer exists


      //  Reference Lifetime
      fn main(){
          {
              let x = 42; // `x` starts existing
              let x_ref =  &x; // `x_ref` starts existing which is a reference to the Variable `x`, also called as `x_ref` borrows `x`
             println!("x_ref = {}", x_ref);
            // `x_ref` stops existing
            // `x` stops existing
          }
      }
            // `x` no longer exists



        // Lifetime of a Reference cannot exceeds that of the borrrowed Variable Bindings
        fn main(){
            let x_ref = {
                let x = 42;
                &x
            };
            println!("x_ref = {}", x_ref);
            // error: `x` does not live long enough, 
            // Because the lifetime of variable x is limited the to internal block only and now the variable x does not exists outside of the block.
            // So, it cannot to borrrowed to a Reference Variable.
      }
    ```

#### Borrowing Multiple Times:
- While borrrowed, the variable cannot be mutated.
- While borrrowed, the variable cannot be mutably borrrowed.


#### Borrowing with Functions
- References in function arguments also have a lifetime.
    - This exists for entire function call.
- A function can be called with borrows (borrrowed variable) that have different lifetime.
- So, to support borrows with different lifetime, 
    - All functions that take references are generic
    - Lifetime are generic parameter in the function 


#### Lifetime
- Lifetime's name start with a single quote, `'` and a name. Eg: `'a`
- There is a special lifetime, named `'static`, which is valid for the entire program's lifetime.




