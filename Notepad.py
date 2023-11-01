import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser, simpledialog

class AdvancedNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        self.text_area = tk.Text(self.root, wrap='word', font=('Arial', 12))
        self.text_area.pack(expand=True, fill='both')

        # Create Menu
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Exit", command=self.exit_app, accelerator="Ctrl+Q")
        menubar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.undo_text, accelerator="Ctrl+Z")
        edit_menu.add_command(label="Redo", command=self.redo_text, accelerator="Ctrl+Y")
        edit_menu.add_command(label="Cut", command=self.cut_text, accelerator="Ctrl+X")
        edit_menu.add_command(label="Copy", command=self.copy_text, accelerator="Ctrl+C")
        edit_menu.add_command(label="Paste", command=self.paste_text, accelerator="Ctrl+V")
        edit_menu.add_command(label="Find", command=self.find_text, accelerator="Ctrl+F")
        edit_menu.add_command(label="Replace", command=self.replace_text, accelerator="Ctrl+H")
        menubar.add_cascade(label="Edit", menu=edit_menu)

        format_menu = tk.Menu(menubar, tearoff=0)
        format_menu.add_command(label="Change Font", command=self.change_font)
        format_menu.add_command(label="Change Text Color", command=self.change_text_color)
        menubar.add_cascade(label="Format", menu=format_menu)

        tools_menu = tk.Menu(menubar, tearoff=0)
        tools_menu.add_command(label="Word Count", command=self.word_count)
        menubar.add_cascade(label="Tools", menu=tools_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.about_notepad)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menubar)
        self.set_keyboard_shortcuts()

    def set_keyboard_shortcuts(self):
        self.root.bind("<Control-n>", lambda event: self.new_file())
        self.root.bind("<Control-o>", lambda event: self.open_file())
        self.root.bind("<Control-s>", lambda event: self.save_file())
        self.root.bind("<Control-q>", lambda event: self.exit_app())
        self.root.bind("<Control-z>", lambda event: self.undo_text())
        self.root.bind("<Control-y>", lambda event: self.redo_text())
        self.root.bind("<Control-x>", lambda event: self.cut_text())
        self.root.bind("<Control-c>", lambda event: self.copy_text())
        self.root.bind("<Control-v>", lambda event: self.paste_text())
        self.root.bind("<Control-f>", lambda event: self.find_text())
        self.root.bind("<Control-h>", lambda event: self.replace_text())

    def new_file(self):
        self.text_area.delete(1.0, 'end')

    def open_file(self):
        file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file:
            with open(file, 'r') as f:
                self.text_area.delete(1.0, 'end')
                self.text_area.insert('end', f.read())

    def save_file(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file:
            with open(file, 'w') as f:
                f.write(self.text_area.get(1.0, 'end'))

    def exit_app(self):
        if messagebox.askokcancel("Exit", "Do you want to exit?"):
            self.root.destroy()

    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")

    def undo_text(self):
        self.text_area.edit_undo()

    def redo_text(self):
        self.text_area.edit_redo()

    def find_text(self):
        find_string = simpledialog.askstring("Find", "Enter text to find:")
        if find_string:
            start = self.text_area.search(find_string, "1.0", stopindex="end", nocase=1)
            if start:
                end = f"{start}+{len(find_string)}c"
                self.text_area.tag_remove("found", "1.0", "end")
                self.text_area.tag_add("found", start, end)
                self.text_area.tag_config("found", background="yellow", foreground="black")
                self.text_area.mark_set("insert", end)
                self.text_area.see("insert")
            else:
                messagebox.showinfo("Not Found", f"Couldn't find '{find_string}'")

    def replace_text(self):
        find_string = simpledialog.askstring("Replace", "Enter text to replace:")
        replace_string = simpledialog.askstring("Replace", f"Replace '{find_string}' with:")
        if find_string:
            start = self.text_area.search(find_string, "1.0", stopindex="end", nocase=1)
            if start:
                end = f"{start}+{len(find_string)}c"
                self.text_area.delete(start, end)
                self.text_area.insert(start, replace_string)
            else:
                messagebox.showinfo("Not Found", f"Couldn't find '{find_string}'")

    def change_font(self):
        font = filedialog.askopenfilename()
        if font:
            self.text_area.configure(font=(font, 12))

    def change_text_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.text_area.config(fg=color)

    def word_count(self):
        text = self.text_area.get(1.0, 'end')
        word_count = len(text.split())
        messagebox.showinfo("Word Count", f"Total words: {word_count}")

    def about_notepad(self):
        messagebox.showinfo("About", "Notepad\nCreated by Your Name")
    def about_notepad(self):
        about_info = (
            """
    About Notepad Application

    Version: 1.0

    Description:
    Notepad is a simple text editor built with Python and Tkinter. It provides basic text editing capabilities such as opening, saving, copying, cutting, pasting, undo, and redo. It's a versatile tool for creating and editing text files.

    Features:
    - Open and edit text files
    - Save files with ease
    - Cut, copy, and paste text
    - Undo and redo actions
    - Basic text formatting
    - User-friendly interface

    Credits:
    - Developed by SE A G7 Group
    - Built with Python and Tkinter
    
    """
        )
        messagebox.showinfo("About", about_info)
def main():
    root = tk.Tk()
    root.geometry("800x600")
    notepad = AdvancedNotepad(root)
    root.mainloop()

if __name__ == "__main__":
    main()
