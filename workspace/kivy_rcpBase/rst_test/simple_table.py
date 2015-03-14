from kivy.app import App
from kivy.uix.rst import RstDocument
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class MyBoxLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        rt = RstDocument(text='''

Table 1 :

+--------------------------------+-------------------------------+
| Lorem ipsum lorem ipsum        | Lorem ipsum                   |
| Lorem ipsum lorem ipsum Lorem  |                               | 
+--------------------------------+-------------------------------+
| Lorem ipsum lorem ipsum        | Lorem ipsum lorem ipsum Lorem | 
| Lorem ipsum lore               | Lorem ipsum lorem ipsum       | 
|                                | Lorem i                       |
|                                |                               |
+--------------------------------+-------------------------------+


''')
#         mytable2 = RstDocument(text='''
# +---------+--------------------------------+-------------------------------+
# | Lorem i | Lorem Ipsum Lorem Ipsum Lorem  |      Lorem Ipsum Lorem        |
# |         | Lorem Ipsum Lorem Ipsum Lorem  |                               |
# |         | Lorem Ipsum Lorem Ipsum Lorem  |                               |
# |         | Lorem Ipsum Lorem Ipsum Lorem  |                               |
# |         | Lorem Ipsum Lorem Ipsum Lorem  |                               |
# |         | Lorem Ipsum Lorem Ipsum Lorem  |                               |
# +=========+================================+===============================+
# | 1 row   | Lorem Ipsum Lorem Ipsum Lo     | Lorem Ipsum Lorem Ipsum Lorem |
# |         | Lorem Ipsum Lorem Ipsum Lo     | Lorem Ipsum Lorem             |
# |         | Lorem Ips                      |                               |
# +---------+--------------------------------+-------------------------------+
# | 2 row   | Lorem Ipsum Lorem Ipsum Lo     | Lorem Ipsum Lorem Ips         |
# |         | Lorem Ipsum Lorem Ips          | Lorem Ipsum Lore              |
# |         | Lorem Ipsum Lorem Ipsum Lorem  |                               |
# |         | Lorem Ipsum Lorem Ipsum        |                               |
# +---------+--------------------------------+-------------------------------+
# | 3 row   | Lorem Ipsum Lorem Ipsum Lo     | Lorem Ipsum Lorem Ipsum Lorem |
# |         | Lorem Ipsum Lorem Ipsum        | Lorem Ipsum Lorem Ipsum Lorem |
# |         | Lorem Ipsum Lorem Ipsum        | Lorem Ipsum Lo                |
# |         | Lorem Ipsum Lorem Ipsum        |                               |
# +---------+--------------------------------+-------------------------------+
# ''')
        btn = Button(text= "My BUTTON")
        self.add_widget(btn)
        self.add_widget(rt)
        

class Simple_TableApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == "__main__":
    Simple_TableApp().run()