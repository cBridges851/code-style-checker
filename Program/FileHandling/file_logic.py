from tkinter import filedialog

class FileLogic:
    def open_file(self, root):
        root.filename = filedialog.askopenfilename(
            initialdir="C:/", 
            title="Select a file", 
            filetypes=(("JavaScript files", ".js"), ("All Files", "*.*"))
            )