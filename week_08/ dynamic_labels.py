from kivy.app import App
from kivy.lang import Builder

class DynamicLabelsApp(App):
    names = ['Alice', 'Bob', 'Charlie', 'David']

    def build(self):
        return Builder.load_file('dynamic_labels.kv')

DynamicLabelsApp().run()
