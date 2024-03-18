from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import StringProperty , ListProperty
import os
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
from kivy.config import Config
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')
resource_add_path('./font')
LabelBase.register(DEFAULT_FONT, 'NotoSerifJP-Black.otf') 


kv_file_path = os.path.join(os.path.dirname(__file__), 'Kv_files', 'test.kv' )
Builder.load_file(kv_file_path)  

class TextWidget(Widget):
    text = StringProperty()
    color = ListProperty([1,1,1,1])

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = 'start'

    def buttonClicked(self):
        self.text = 'おはよう'
        self.color = [1, 0, 0 , 1]
    
    def buttonClicked2(self):
        self.text = 'こんにちは'
        self.color = [0, 1, 0 , 1 ]

    def buttonClicked3(self):
        self.text = 'こんばんは'
        self.color = [0, 0, 1 , 1 ]



class Test(App):
        
        def __init__(self, **kwargs):
            super(Test, self).__init__(**kwargs)
            self.title = '挨拶'

        def build(self):
            return TextWidget()
            
if __name__=='__main__':
    Test().run()


