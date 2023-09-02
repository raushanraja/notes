#### State Pattern:
- State pattern allows an object to change its behavior when its internal state changes.
- Which it changes internal state, object seems to change its class.
- Example: Implementing a turnstile with different states (e.g., locked, unlocked).
- It Comprises of three main components: Context, State, and Subclass.
- The pattern extract state-realted behavior into seperate state classes (State Subclass)
- The original Context object delegates the work to an instance of subsclass, instead 
of action on it's own.

#### Context:
- Context contains a state variable that holds the current instance of the State Subclass.
- It Provides an interface/method for the State Subclass to:
    - Update the state variable.
    - Update the reference to the context in the State Subclass.

#### State & Subclass:
- State is an interface implemented by State Subclasses.
- The State interface defines required members that are set by its subclasses.
- It includes required methods for various actions based on the state.
- Subclass objects represent different states.

