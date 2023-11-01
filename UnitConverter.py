import tkinter as tk
from tkinter import ttk


class AdvancedUnitConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Unit Converter")
        self.root.geometry("400x300")

        self.unit_converter = UnitConverter()

        self.label_from = ttk.Label(root, text="From Category:")
        self.label_from.grid(row=0, column=0, padx=10, pady=10)

        self.from_category = ttk.Combobox(root, values=self.unit_converter.get_categories())
        self.from_category.grid(row=0, column=1, padx=10, pady=10)
        self.from_category.set("Length")

        self.label_to = ttk.Label(root, text="To Category:")
        self.label_to.grid(row=1, column=0, padx=10, pady=10)

        self.to_category = ttk.Combobox(root, values=self.unit_converter.get_categories())
        self.to_category.grid(row=1, column=1, padx=10, pady=10)
        self.to_category.set("Length")

        self.label_from_unit = ttk.Label(root, text="From Unit:")
        self.label_from_unit.grid(row=2, column=0, padx=10, pady=10)

        self.from_unit = ttk.Combobox(root, values=self.unit_converter.get_units(self.from_category.get()))
        self.from_unit.grid(row=2, column=1, padx=10, pady=10)
        self.from_unit.set("Meter")

        self.label_to_unit = ttk.Label(root, text="To Unit:")
        self.label_to_unit.grid(row=3, column=0, padx=10, pady=10)

        self.to_unit = ttk.Combobox(root, values=self.unit_converter.get_units(self.to_category.get()))
        self.to_unit.grid(row=3, column=1, padx=10, pady=10)
        self.to_unit.set("Feet")

        self.label_value = ttk.Label(root, text="Value:")
        self.label_value.grid(row=4, column=0, padx=10, pady=10)

        self.value_entry = ttk.Entry(root)
        self.value_entry.grid(row=4, column=1, padx=10, pady=10)

        self.convert_button = ttk.Button(root, text="Convert", command=self.convert_units)
        self.convert_button.grid(row=5, columnspan=2, padx=10, pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.grid(row=6, columnspan=2, padx=10, pady=10)

        self.from_category.bind("<<ComboboxSelected>>", self.update_from_units)
        self.to_category.bind("<<ComboboxSelected>>", self.update_to_units)

    def convert_units(self):
        from_category = self.from_category.get()
        to_category = self.to_category.get()
        from_unit = self.from_unit.get()
        to_unit = self.to_unit.get()
        value = self.value_entry.get()

        try:
            value = float(value)
            result = self.unit_converter.convert(from_category, to_category, from_unit, to_unit, value)
            self.result_label.config(text=f"Result: {result:.4f} {to_unit}")
        except ValueError:
            self.result_label.config(text="Invalid input (numeric value required)")
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")

    def update_from_units(self, event):
        category = self.from_category.get()
        units = self.unit_converter.get_units(category)
        self.from_unit["values"] = units
        self.from_unit.set(units[0])

    def update_to_units(self, event):
        category = self.to_category.get()
        units = self.unit_converter.get_units(category)
        self.to_unit["values"] = units
        self.to_unit.set(units[0])

class UnitConverter:
    def __init__(self):
        # Define conversion factors for various categories
        self.conversion_factors = {
            "Length": {
                "Meter": 1.0,
                "Feet": 3.28084,
                "Yard": 1.09361,
                "Inch": 39.3701,
            },
            "Mass": {
                "Kilogram": 1.0,
                "Pound": 2.20462,
                "Ounce": 35.274,
                "Gram": 1000,
            },
            "Temperature": {
                "Celsius": (1, 0),
                "Fahrenheit": (1.8, 32),
                "Kelvin": (1, 273.15),
            },
            # Add more categories and units here
        }

        # Get all supported categories
        self.categories = list(self.conversion_factors.keys())

    def get_categories(self):
        return self.categories

    def get_units(self, category):
        if category in self.conversion_factors:
            return list(self.conversion_factors[category].keys())

    def convert(self, from_category, to_category, from_unit, to_unit, value):
        if from_category == to_category:
            if from_unit == to_unit:
                return value
            if from_unit in self.conversion_factors[from_category]:
                conversion_factor = self.conversion_factors[from_category][to_unit]
                if isinstance(conversion_factor, tuple):
                    return (value - conversion_factor[1]) * conversion_factor[0]
                return value * conversion_factor
            else:
                raise ValueError("Invalid 'From Unit'")
        else:
            raise ValueError("Category mismatch: 'From Category' and 'To Category' must be the same")

def main():
    root = tk.Tk()
    app = AdvancedUnitConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
