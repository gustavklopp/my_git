import kivy
from kivy.app import App
from kivy.uix.rst import RstDocument
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MyBoxLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # create a default grid layout with custom width/height
        self.size_hint_y = None
        self.bind(minimum_height=self.setter('height'))
        self.cols = 1
        
        for box in range(15):
            btn = Button(text="Button "+ str(box), height="30dp",
                     size_hint_y=None)
            lbl = RstDocument(text= '''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam viverra, justo vel faucibus lacinia, sapien eros scelerisque erat, cursus lacinia urna turpis quis lacus. Donec vitae augue urna. Integer eu nunc lorem. Fusce vulputate mi neque, ac tristique augue molestie vitae. Ut tincidunt urna a lectus egestas, quis eleifend nunc aliquam. Praesent id viverra sem. Suspendisse faucibus orci sed ipsum varius euismod. 
   
    +------------------+---------------------------+--------------------------------+
    |    Column A      |      Column B             |        Column C                |
    +------------------+---------------------------+--------------------------------+
    | Lorem ipsum dolor|   Lorem ipsum dolor       |   Lorem ipsum dolor            |
    | sit amet, consec |   sit amet, consectetur   |   sit amet, consectetur        |
    |                  |   adipiscing elit. Etiam  |   adipiscing elit. Etiam viver |
    +------------------+---------------------------+--------------------------------+
    |       Lorem      |    Lorem                  |    Etiam viverra, justo        |
    |                  |                           |    vel faucibus lacinia        |
    +------------------+---------------------------+--------------------------------+
    
    Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec suscipit metus ac viverra auctor.           
    '''
    , height="300dp", size_hint_y=None
    )
            self.add_widget(btn)
            self.add_widget(lbl)
        

class RstTestApp(App):
    pass

if __name__ == "__main__":
    RstTestApp().run()