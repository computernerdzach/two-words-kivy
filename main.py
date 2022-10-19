from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from random import randint

from words import words


class MyLayout(BoxLayout):
    def __init__(self):
        super().__init__()

        self.button = Button(text='Two Words',
                             background_normal='',
                             background_color="#0096FF")
        self.button.bind(on_press=self.press_color)
        self.button.bind(on_release=self.get_words)
        self.add_widget(self.button)

    def get_words(self, button):
        self.button.background_color = '#0096FF'
        index1, index2 = randint(0, len(words)), randint(0, len(words))
        while index1 == index2:
            index2 = randint(0, len(words))
        self.button.text = f'{words[index1].upper()}       and       {words[index2].upper()}'

    def press_color(self, button):
        self.button.background_normal = ''
        self.button.background_color = '#FA8072'


class MyApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()
