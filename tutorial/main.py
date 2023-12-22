from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class Interface(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        btn = Button(text="Click Me!", size_hint=(0.5,0.5), pos_hint={"center_x":0.5, "center_y":0.5})
        btn.bind(on_press=self.button_press)
        self.add_widget(btn)

    def button_press(self, obj):
        print(obj.text)
        #print(obj.size)

class FirstApp(App):
    pass

FirstApp().run()
