import tkinter as tk
from PIL import Image, ImageTk
from subprocess import call


def execute_file(file_name):
    call(["python", file_name])


class StyledButton(tk.Button):
    def __init__(self, master, image_file, text, command):
        img = Image.open(image_file)
        img = img.resize((100, 100))  # Resize the image to fit the button
        photo = ImageTk.PhotoImage(img)

        super().__init__(master, image=photo, compound=tk.TOP, text=text, command=command, width=150, height=150)
        self.configure(
            bg="#3498db",
            fg="white",
            relief="flat",
            font=("Arial", 12, "bold")
        )
        self.image = photo  # Keep a reference to avoid garbage collection


root = tk.Tk()
root.title("ToolMaster")


def run_calculator():
    execute_file("Calculator.py")


def run_currency_converter():
    execute_file("CurrencyConverter.py")


def run_notepad():
    execute_file("Notepad.py")


def run_qr_code_generator():
    execute_file("QRCodeGenerator.py")


def run_unit_converter():
    execute_file("UnitConverter.py")


button1 = StyledButton(root, "Calculator.png", "Calculator", run_calculator)
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = StyledButton(root, "CurrencyConverter.png", "Currency Converter", run_currency_converter)
button2.grid(row=0, column=1, padx=10, pady=10)

button3 = StyledButton(root, "Notepad.png", "Notepad", run_notepad)
button3.grid(row=1, column=0, padx=10, pady=10)

button4 = StyledButton(root, "QRCodeGenerator.png", "QR Code Generator", run_qr_code_generator)
button4.grid(row=1, column=1, padx=10, pady=10)

button5 = StyledButton(root, "UnitConverter.png", "Unit Converter", run_unit_converter)
button5.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
