## Type Aliases
- Type alias creates a name for another type.
- Aliases and original type can be used interchangeably.
- `type` keyboard is used to create an alias.
```rust
enum CarryableConcreteItem {
    Left, 
    Right
}

// Creating an alias
type Item  = CarryableConcreteItem;

use std::cell::RefCell;
use std::sync::{Arc, RwLock};

// Creating another alias
type PlayerInventory = RwLock<Vec<Arc<RefCell<Item>>>>;
```
