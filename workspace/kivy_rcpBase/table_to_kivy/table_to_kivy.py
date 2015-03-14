from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.rst import RstDocument
from kivy.app import App



class MyLabelWithBackground(Label):
    pass

class MyHBoxLayout(BoxLayout):
    pass

class Demo(GridLayout):
    pass


class TableToKivyApp(App):
    def build(self):
        return Demo()

if __name__ == '__main__':
    TableToKivyApp().run()
