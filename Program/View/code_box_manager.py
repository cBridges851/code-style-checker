import tkinter as tk
from FileHandling.file_logic import FileLogic


class CodeBoxManager:
    def clear_code_box(self, code_box):
        """
            Removes placeholder text from the box where the user inputs their code.
            Args:
                code_box: ScrolledText, the box where the user inputs their code.
        """
        if code_box.get("1.0", tk.END) == "Input JavaScript Code Here...\n":
            code_box.delete("1.0", tk.END)

    def insert_placeholder(self, root, code_box):
        """
            Puts in the placeholder if there is nothing in the box.
            Args:
                code_box: ScrolledText, the box where the user inputs their code.
        """
        if code_box.get("1.0", tk.END) == "\n":
            code_box.insert(tk.END, "Input JavaScript Code Here...")

    def display_file_contents(self, root, code_box):
        """
            Displays all the lines that are in a JavaScript file that has been
            imported via the file explorer.
            Args:
                root: Tk, the root of the application
                code_box: ScrolledText, the box where the code will be inserted into.
        """
        lines = FileLogic().open_file(root)

        if lines != None:
            # Clear output box
            code_box.delete("1.0", tk.END)

            # Output lines into input box.
            for line in lines:
                code_box.insert(tk.END, line)