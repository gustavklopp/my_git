import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen




class MenuScreen(Screen):
#     def switching_function(*args):
#         global sm
#         sm.current = 'Server'

    def __init__(self, **kwargs):

        super(MenuScreen, self).__init__(**kwargs)


        def Server(instance):
            self.clear_widgets()
            self.add_widget(Label ( text = 'Inside server function'))
            server = ServerScreen()
            #return server
            #server.function()

        self.add_widget(Label ( text = 'What Type Of Service You Want...???'))

        button1 = Button(text = 'Server',size_hint = (None,None),pos = (0,0))
        self.add_widget(button1)
        button1.bind(on_press = Server)
#         button1.bind(on_press = self.switching_function)

        button2 = Button(text = 'Client',size_hint = (None,None),pos = (100,0))
        self.add_widget(button2)
        #button2.bind(on_press = Client)




class ServerScreen(Screen):

    def __init__(self, **kwargs):
        super(ServerScreen, self).__init__(**kwargs)
        print('Inside server screen')

        self.clear_widgets()
        self.add_widget(Label (text = 'Working As A Server'))
        print("Hellooooooooooo")


sm = ScreenManager()
sm.add_widget(MenuScreen(name='Menu'))
sm.add_widget(ServerScreen(name='Server'))
#sm.add_widget(ClientScreen(name='Client'))    

class FileApp(App):

    def build(self):

        #return Menu()

        return sm

if __name__ == '__main__':
    FileApp().run()