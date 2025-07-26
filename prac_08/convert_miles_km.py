"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
Lindsay Ward, IT@JCU
06/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERSION_FACTOR = 1.60934


class MilesConverterApp(App):
    """Convert miles to kilometres with adjustable input and output."""

    output_text = StringProperty()

    def build(self):
        """Load the Kivy GUI."""
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file("convert_miles_km.kv")
        self.output_text = "0.0"
        return self.root

    def handle_convert(self):
        """Convert input to km."""
        self.output_text = str(self.get_miles() * CONVERSION_FACTOR)

    def handle_increment(self, amount):
        """Increase or decrease miles and convert."""
        miles = self.get_miles() + amount
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert()

    def get_miles(self):
        """Get the input miles as a float. Return 0.0 if invalid."""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0


MilesConverterApp().run()
# Dummy change to trigger pull request
