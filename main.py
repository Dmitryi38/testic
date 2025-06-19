import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

kivy.require('2.1.0')  # replace with your version of Kivy

class CalculatorApp(App):
    def build(self):
        self.result = TextInput(font_size=32, readonly=True, halign="right", multiline=False)
        self.result.text = "0"
        
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.result)
        
        # Create grid for the calculator buttons
        button_grid = GridLayout(cols=4)
        
        buttons = [
            ('7', 'images/7.png'),
            ('8', 'images/8.png'),
            ('9', 'images/9.png'),
            ('/', 'images/divide.png'),
            ('4', 'images/4.png'),
            ('5', 'images/5.png'),
            ('6', 'images/6.png'),
            ('*', 'images/multiply.png'),
            ('1', 'images/1.png'),
            ('2', 'images/2.png'),
            ('3', 'images/3.png'),
            ('-', 'images/minus.png'),
            ('0', 'images/0.png'),
            ('C', 'images/clear.png'),
            ('=', 'images/equal.png'),
            ('+', 'images/plus.png'),
        ]
        
        for label, img_path in buttons:
            button = Button(on_press=self.on_button_press)
            button.text = label
            button.background_normal = img_path  # Setting the image as background
            button_grid.add_widget(button)
        
        layout.add_widget(button_grid)
        return layout

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text
        
        if button_text == 'C':  # Clear
            self.result.text = "0"
        elif button_text == '=':  # Equals
            try:
                self.result.text = str(eval(self.result.text))
            except:
                self.result.text = "Error"
        else:  # Number or Operator
            if current == "0" and button_text not in ['+', '-', '/', '*']:
                self.result.text = button_text
            else:
                self.result.text = current + button_text

if __name__ == '__main__':
    CalculatorApp().run()



    #Заебала
