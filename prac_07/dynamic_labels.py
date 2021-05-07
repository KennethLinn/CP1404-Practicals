from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelGeneratorApp(App):
    def __init__(self):
        super().__init__()
        self.names = ['Steve', 'Tony', 'Bucky', 'Sam', 'Rhody', 'Bruce']

    def build(self):
        self.title = 'Dynamic Label Generator'
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelGeneratorApp().run()
