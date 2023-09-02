from abc import abstractmethod
from typing import Optional


class State:

    # A State Subclass is Inherited from State class
    # This state class actually is a interface
    # This class have few state varialbes, methods
    # and maybe a back-reference to the context

    @property
    def context(self) -> 'Context':
        return self._context

    @context.setter
    def context(self, context: 'Context') -> None:
        self._context = context

    @abstractmethod
    def alert(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def update_state(self) -> None:
        raise NotImplementedError()


class Context:
    # The Context contains the interfaces used by clients
    # This contains required state variable
    # This keeps track of current instance of a State Subclass
    # This state variable also represents the current state of context

    # A State Subclass is Inherited from State class
    # This state class actually is a interface
    # This class have few state varialbes, methods
    # and maybe a back-reference to the context

    _state = None  # This keeps track of current instance of state subclass object

    def __init__(self, state: State) -> None:
        self.update_state(state)

    def update_state(self, state: State):
        self._state = state
        self._state.context = self

    def alert(self):
        if self._state:
            self._state.alert()
            return
        raise AttributeError()


class Vibration(State):
    def alert(self) -> None:
        print("Vibration...")

    def update_state(self, state: Optional[State] = None):
        if state:
            self.context.update_state(state)
        else:
            self.context.update_state(Silent())


class Silent(State):
    def alert(self) -> None:
        print("Silent...")

    def update_state(self, state: Optional[State] = None):
        if state:
            self.context.update_state(state)
        else:
            self.context.update_state(Vibration())


silent = Silent()
vibration = Vibration()

ctx = Context(state=silent)
ctx.alert()

ctx.update_state(state=vibration)
ctx.alert()

vibration.update_state(silent)
ctx.alert()

silent.update_state(vibration)
ctx.alert()

ctx.update_state(silent)
ctx.alert()

ctx.update_state(vibration)
ctx.alert()
