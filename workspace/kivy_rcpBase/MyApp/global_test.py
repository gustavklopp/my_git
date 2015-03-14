from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivy.properties import ObjectProperty



class FirstScreen(Screen):
    obj_input = ObjectProperty()
    obj_label = ObjectProperty()
           
    def buttonClicked(self):
        print('RESULT :', self.obj_input.text)
        self.obj_label.text = "You wrote : " + self.obj_input.text
            

class SecondScreen(Screen):
        
    obj_input1_box = ObjectProperty()
    
    def update_text(self, label_text):
        print('label_text :', label_text)
        self.obj_input1_box.text = label_text



class Global_VariableApp(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(FirstScreen(name='firstcreen'))
        sm.add_widget(SecondScreen(name='secondscreen')) 
        return sm


if __name__ == "__main__":
    Global_VariableApp().run()