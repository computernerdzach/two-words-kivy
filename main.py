from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from random import randint

from words import words


class MyLayout(BoxLayout):
    def __init__(self):
        super().__init__()
        self.words = list()

        self.button = Button(text='Two Words')
        self.button.bind(on_press=self.get_words)
        self.add_widget(self.button)

    def get_words(self, button):
        self.words = []
        index1 = randint(0, len(words))
        index2 = index1
        while index1 == index2:
            index2 = randint(0, len(words))
        self.words.append(words[index1])
        self.words.append(words[index2])
        self.button.text = f'{self.words[0].upper()}       and       {self.words[1].upper()}'


class MyApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()
