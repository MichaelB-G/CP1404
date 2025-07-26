from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """App that dynamically creates labels from a list."""

    def build(self):
        """Load the GUI and populate labels."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")

        # Your list of names
        names = ["Michael", "Amie", "Lindsay", "Persephone", "Gharma"]

        for name in names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)

        return self.root


DynamicLabelsApp().run()
