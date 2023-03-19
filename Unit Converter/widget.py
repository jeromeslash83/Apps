import tkinter as tk
from tkinter import ttk
from converter import Converter


class ConverterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Unit Converter")
        self.geometry("400x300")
        self.resizable(False, False)
        self.converter = Converter()

        # Set a custom style
        style = ttk.Style()
        style.configure('TButton', background='#3C3F41', foreground='white', font=('Helvetica', 14))
        style.configure('TLabel', background='#3C3F41', foreground='white', font=('Helvetica', 14))
        style.configure('TEntry', background='#3C3F41', foreground='white', font=('Helvetica', 14))
        style.configure('TOM.TMenubutton', background='#3C3F41', foreground='white', font=('Helvetica', 14))
        style.configure('TOM.TMenubutton.Menu', background='white', foreground='black', font=('Helvetica', 14))
        style.configure('ConvertButton.TButton', background='gold', foreground='black', font=('Helvetica', 14))
        self.configure(bg='#3C3F41')

        self.create_widgets()

    def create_widgets(self):
        self.conversion_options = [
            "Fahrenheit to Celsius",
            "Celsius to Fahrenheit",
            "Centimeter to Inches",
            "Inches to Centimeter",
            "Feet to Centimeter",
            "Centimeter to Feet",
            "Kilometer to Miles",
            "Miles to Kilometer",
            "Inches to Feet",
            "Feet to Inches"
        ]

        self.option_var = tk.StringVar()
        self.option_var.set(self.conversion_options[0])

        self.option_menu = ttk.OptionMenu(
            self, self.option_var, self.conversion_options[0], *self.conversion_options, style='TOM.TMenubutton')
        self.option_menu.pack(pady=20)

        self.input_value = tk.StringVar()

        self.entry = ttk.Entry(self, textvariable=self.input_value, foreground='black', background='#3C3F41',
                               font=('Helvetica', 14))
        self.entry.pack(pady=10)

        self.convert_button = ttk.Button(
            self, text="Convert", command=self.perform_conversion, style='ConvertButton.TButton')
        self.convert_button.pack(pady=10)

        self.result_label = ttk.Label(self, text="")
        self.result_label.pack(pady=10)

    def perform_conversion(self):
        conversion_type = self.option_var.get()
        value = float(self.input_value.get())
        result = None

        if conversion_type == "Fahrenheit to Celsius":
            result = self.converter.fahrenheit_to_celsius(value)
        elif conversion_type == "Celsius to Fahrenheit":
            result = self.converter.celsius_to_fahrenheit(value)
        elif conversion_type == "Centimeter to Inches":
            result = self.converter.cm_to_inches(value)
        elif conversion_type == "Inches to Centimeter":
            result = self.converter.inches_to_cm(value)
        elif conversion_type == "Feet to Centimeter":
            result = self.converter.feet_to_cm(value)
        elif conversion_type == "Centimeter to Feet":
            result = self.converter.cm_to_feet(value)
        elif conversion_type == "Kilometer to Miles":
            result = self.converter.km_to_miles(value)
        elif conversion_type == "Miles to Kilometer":
            result = self.converter.miles_to_km(value)
        elif conversion_type == "Inches to Feet":
            result = self.converter.inches_to_feet(value)
        elif conversion_type == "Feet to Inches":
            result = self.converter.feet_to_inches(value)

        self.result_label.configure(text=f"Result: {result:.2f}")


