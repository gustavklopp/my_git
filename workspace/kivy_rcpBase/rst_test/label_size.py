from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

Builder.load_string('''
<MyLabel>
    canvas:
        Color:
            rgba: 0, 1, 0, 0.5
        Rectangle:
            pos: self.pos
            size: self.size
''')


class MyLabel(Label):
    pass

class MyApp(App):
    def build(self):
        root = FloatLayout()

        b = GridLayout(
            cols=1,
            size_hint=(None, None),
            spacing=20,
            width=200)
        b.bind(minimum_height=b.setter('height'))
        root.add_widget(b)

  
        l = MyLabel(
            text='word ' * 80,
            size_hint_y=None, padding = [-5,5])
        l.bind(width=lambda s, w:
               s.setter('text_size')(s, (w, None)))
        l.bind(texture_size=l.setter('size'))
        b.add_widget(l)

        return root


if __name__ == '__main__':
    MyApp().run()

