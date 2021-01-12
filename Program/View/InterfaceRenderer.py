# from tkinter import Tk, Label, Button
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class InterfaceRenderer:
    def __init__(self):
        self.root = tk.Tk()
        self.box_width = 50
        self.primary_bg_colour = "#1D1D1D"
        self.secondary_bg_colour = "#2D2D2D"

    def clear_code_box(self, code_box):
        if code_box.get("1.0", tk.END) == "Input JavaScript Code Here...\n":
            code_box.delete("1.0", tk.END)

    def insert_placeholder(self, code_box):
        if code_box.get("1.0", tk.END) == "\n":
            code_box.insert(tk.END, "Input JavaScript Code Here...")

    def render_window(self):
        self.root.iconbitmap("view/favicon.ico")
        self.root.title("Chrispy Code Style Checker")
        self.root.resizable(False, False)
        self.root.configure(bg=self.primary_bg_colour, padx=10, pady=10)

    def render_title(self):
        title_label = tk.Label(self.root, text="Chrispy Code Style Checker")
        title_label.configure(bg=self.primary_bg_colour, fg="#FFFFFF", font=("Helvetica 26 bold"))
        title_label.grid(row=0, column=0)

    def render_code_input_box(self):
        code_box = ScrolledText(self.root)
        code_box.configure(width=self.box_width, height=15, bg=self.secondary_bg_colour, fg="#C2C0C0", font=("Consolas 14"))
        self.insert_placeholder(code_box)
        code_box.bind("<Button 1>", lambda event: self.clear_code_box(code_box))
        code_box.bind("<FocusOut>", lambda event: self.insert_placeholder(code_box))
        code_box.grid(row=1, column=0)

    def render_validate_button(self):
        validate_button = tk.Button(self.root, text="VALIDATE!")
        validate_button.configure(width=41, font=("Helvetica 14"), bg="#7A7A7A")
        validate_button.grid(row=2, column=0, pady=10)

    def render_output_box(self):
        output_box = ScrolledText(self.root)
        output_box.configure(width=self.box_width, height=7, bg=self.secondary_bg_colour, state="disabled", font=("Consolas 14"))
        output_box.grid(row=3, column=0)

    def render_interface(self):
        self.render_window()
        self.render_title()
        self.render_code_input_box()
        self.render_validate_button()
        self.render_output_box()
        self.root.mainloop()
