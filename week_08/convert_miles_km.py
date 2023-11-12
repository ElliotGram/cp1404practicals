from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_CONVERSION = 1.60934  # Constant for conversion factor


class MilesToKmConverter(App):
    output_result = StringProperty("0.0")

    def build(self):
        return Builder.load_file('convert_miles_km.kv')

    def handle_conversion(self):
        try:
            miles = float(self.root.ids.input_miles.text)
            kilometers = miles * MILES_TO_KM_CONVERSION
            self.output_result = str(kilometers)
        except ValueError:
            self.output_result = "0.0"

    def handle_increment(self, value):
        try:
            miles = float(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0.0
        miles += value
        self.root.ids.input_miles.text = str(miles)
        self.handle_conversion()


MilesToKmConverter().run()
