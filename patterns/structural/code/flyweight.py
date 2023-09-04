from abc import ABC, abstractmethod


# Flyweight Interface
class CharacterStyleInterface(ABC):
    @abstractmethod
    def render(self, character, position):
        raise NotImplemented()


# Flyweight
class CharacterStyle(CharacterStyleInterface):
    '''Here we are creatig a Flyweight, which has two interensic state.
       And extrensic state is passed in the render method using paramters.
    '''

    def __init__(self, font, color) -> None:
        self.font = font
        self.color = color

    def render(self, character, position):
        print(
            f"Character '{character}' at position {position} with font '{self.font}' and color '{self.color}'")


# Flyweight Factory
class CharacterStyleFactory:
    '''This factory handles CharacterStyle object creation and
       keeps a cache of such object, so they are not created again.
    '''

    _styles = {}

    @staticmethod
    def get_style(font, color):
        if (font, color) not in CharacterStyleFactory._styles:
            __style = CharacterStyle(font, color)
            CharacterStyleFactory._styles[(font, color)] = __style
        return CharacterStyleFactory._styles[(font, color)]


# Client
class TextEditor:
    '''Client that adds characters with specific styles and then renders the text.'''

    def __init__(self) -> None:
        self.characters = []

    def add_character(self, character, font, color, position):
        style = CharacterStyleFactory.get_style(font, color)
        self.characters.append((character, style, position))

    def render_text(self):
        for character, style, position in self.characters:
            style.render(character, position)


if __name__ == '__main__':
    editor = TextEditor()

    editor.add_character("H", "Arial", "Red", (0, 0))
    editor.add_character("e", "Arial", "Red", (10, 0))
    editor.add_character("l", "Arial", "Blue", (20, 0))
    editor.add_character("l", "Arial", "Blue", (30, 0))
    editor.add_character("o", "Times New Roman", "Green", (40, 0))

    editor.render_text()
