# Topics:
- Threads
- Channels
    - Unbounded
    - Bounded 
- Send Trait & Sync Trait
- Shared State
    - Arc<T>
    - Mutex<T>
- Async
- Future
- Runtimes
    - Tokio
    - async-std
    - smol
- Futures Control Flow
    - Join
    - Select
- Pitfalls of async/await
    - Blocking the Executor
    - Pin
    - Async Traits
    - Cancellation



# Sharing Data between threads
- ***"do not communicate by sharing memory.”***

## Common Concurrency Primitives:
### MUTEX (Mutual Exclusion)
- Steps to share data between mutliple threads safely using MUTEX
    - Wrap the data with Mutex::new(data)
    - Wrap the wrapped Mutex with Arc::new(Mutex::new(data))
    - Clone the Arc<Mutex<T>> and use it.
- How does it works:
    - Mutex<T> is a smart pointer which provides interior mutability, i.e the data inside a mutex can be mutated.
    - ARC "Atomic Reference Counter" provides safe way to clone the Mutex data when cloned, the ARC Counter is incremented and it's subtracted once the clone is dropped.
    - So, when an ARC Mutex is cloned, it allows mutating the data wrapped within Mutex by acquaring a lock and when it goes out of scoped the lock is removed,
    so mutliple threads can mutate but once at a time.

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main(){
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];
    
    for _ in 0..10 {
        let counter = Arc::clone(&counter);
        let handle = thread::spawn(move ||{
            let mut num = counter.lock().unwrap();
            *num +=1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }
    println!("Result: {}", *counter.lock().unwrap());
}
```
