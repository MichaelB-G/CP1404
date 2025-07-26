from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """A simple GUI app for greeting the user."""

    def build(self):
        """Load the .kv layout file."""
        self.title = "BoxLayout Demo"
        self.root = Builder.load_file("box_layout.kv")
        return self.root

    def handle_greet(self):
        """Display a greeting using the input name."""
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"

    def handle_clear(self):
        """Clear the input and output fields."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


BoxLayoutDemo().run()
