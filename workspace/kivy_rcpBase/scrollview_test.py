import kivy
import string

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Rectangle, Color

class longTextLabelApp(App):

    def build(self):

        scrollViewLayout = ScrollView(do_scroll_x=False)
        childLayout = GridLayout(cols = 1, size_hint_x = 1, size_hint_y = None)
        childLayout.bind(minimum_height=childLayout.setter('height'))

        def longTextLabel():
            _long_text = """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus odio nisi, pellentesque molestie adipiscing vitae, aliquam at tellus. Fusce quis est ornare erat pulvinar elementum ut sed felis. Donec vel neque mauris. In sit amet nunc sit amet diam dapibus lacinia. In sodales placerat mauris, ut euismod augue laoreet at. Integer in neque non odio fermentum volutpat nec nec nulla. Donec et risus non mi viverra posuere. Phasellus cursus augue purus, eget volutpat leo. Phasellus sed dui vitae ipsum mattis facilisis vehicula eu justo.

            Quisque neque dolor, egestas sed venenatis eget, porta id ipsum. Ut faucibus, massa vitae imperdiet rutrum, sem dolor rhoncus magna, non lacinia nulla risus non dui. Nulla sit amet risus orci. Nunc libero justo, interdum eu pulvinar vel, pulvinar et lectus. Phasellus sed luctus diam. Pellentesque non feugiat dolor. Cras at dolor velit, gravida congue velit. Aliquam erat volutpat. Nullam eu nunc dui, quis sagittis dolor. Ut nec dui eget odio pulvinar placerat. Pellentesque mi metus, tristique et placerat ac, pulvinar vel quam. Nam blandit magna a urna imperdiet molestie. Nullam ut nisi eget enim laoreet sodales sit amet a felis.
            """
            reallyLongText = _long_text + _long_text + _long_text + _long_text +_long_text
            myLabel = Label(text = reallyLongText, text_size = (700,None), line_height=1.5)

            print("The label size is ", myLabel.size)    
            myLabel.size_hint_y = None
            myLabel.height = 2200

            return myLabel

        childLayout.add_widget(longTextLabel())
        scrollViewLayout.add_widget(childLayout)
        return scrollViewLayout

if __name__ == '__main__':
    longTextLabelApp().run()