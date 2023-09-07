# Abstract FactorY
class GUIFactory:
    def create_button(self):
        raise NotImplementedError("You should implement this method")


class WindowFactory(GUIFactory):
    def create_button(self):
        return WindowButton()


class LinuxFactor(GUIFactory):
    def create_button(self):
        return LinuxButton()


class Button:
    def paint(self):
        raise NotImplementedError("You should implement this method")


class WindowButton(Button):
    def paint(self):
        print("Window Button")


class LinuxButton(Button):
    def paint(self):
        print("Linux Button")
