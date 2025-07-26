"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""
from kivy.app import App
from kivy.lang import Builder


class SquaringApp(App):
    """App to square a number entered by the user."""

    def build(self):
        self.title = "Square Number"
        self.root = Builder.load_file("squaring.kv")
        return self.root

    def handle_calculate(self):
        """Calculate and display the square of the input number."""
        try:
            value = float(self.root.ids.input_number.text)
        except ValueError:
            value = 0.0
        result = value ** 2
        self.root.ids.output_label.text = str(result)


SquaringApp().run()
