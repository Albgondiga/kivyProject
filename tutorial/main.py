from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class Interface(FloatLayout):
    def printing_msg(self):
        print("Hello World!")

class FirstApp(App):
    def printing_msg(self):
        print("Hello World!")

FirstApp().run()
