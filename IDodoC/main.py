from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock


class HelloApp(App):
    def build(self):
        # Vytvoření instance Label
        self.label = Label(text="Ahoj Patriku!", font_size='40sp')

        # Naplánování změny textu po 5 sekundách
        Clock.schedule_once(self.change_text, 5)

        return self.label

    def change_text(self, dt):
        # Změna textu
        self.label.text = "Tak se měj, ahoj."


if __name__ == "__main__":
    HelloApp().run()
