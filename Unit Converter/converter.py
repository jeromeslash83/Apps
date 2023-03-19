class Converter:
    def __init__(self):
        pass

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9 / 5) + 32

    def cm_to_inches(self, cm):
        return cm * 0.393701

    def inches_to_cm(self, inches):
        return inches / 0.393701

    def feet_to_cm(self, feet):
        return feet * 30.48

    def inches_to_feet(self, inches):
        return inches / 12

    def feet_to_inches(self, feet):
        return feet * 12

    def cm_to_feet(self, cm):
        return cm / 30.48

    def km_to_miles(self, km):
        return km * 0.621371

    def miles_to_km(self, miles):
        return miles / 0.621371