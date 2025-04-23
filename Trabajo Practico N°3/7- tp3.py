from abc import ABC, abstractmethod

# Fábricas abstractas y concretas
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_window(self):
        pass

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_window(self):
        return WindowsWindow()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_window(self):
        return MacWindow()

class LinuxFactory(GUIFactory):
    def create_button(self):
        return LinuxButton()

    def create_window(self):
        return LinuxWindow()

# Interfaces abstractas de productos
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class Window(ABC):
    @abstractmethod
    def render(self):
        pass

# Productos concretos
class WindowsButton(Button):
    def render(self):
        return "🪟 Botón estilo Windows"

class WindowsWindow(Window):
    def render(self):
        return "🪟 Ventana estilo Windows"

class MacButton(Button):
    def render(self):
        return "🍏 Botón estilo macOS"

class MacWindow(Window):
    def render(self):
        return "🍏 Ventana estilo macOS"

class LinuxButton(Button):
    def render(self):
        return "🐧 Botón estilo Linux"

class LinuxWindow(Window):
    def render(self):
        return "🐧 Ventana estilo Linux"

# Cliente
def build_gui(factory: GUIFactory):
    button = factory.create_button()
    window = factory.create_window()
    print(button.render())
    print(window.render())

# Simulación
if __name__ == "__main__":
    print("🖥️ Interfaz en Windows:")
    build_gui(WindowsFactory())
    print("\n🍎 Interfaz en macOS:")
    build_gui(MacFactory())
    print("\n🐧 Interfaz en Linux:")
    build_gui(LinuxFactory())
