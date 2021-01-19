from tkinter import filedialog

class FileLogic:
    """
        The class that does the file handling logic for the application.
    """

    def open_file(self, root):
        """
            Allows the user to open a file via the file explorer
            Args:
                root: Tk, the root of the Tkinter program.
            Returns:
                lines: list, contains all the lines that were in the file.
        """
        root.filename = filedialog.askopenfilename(
            initialdir="C:/", 
            title="Select a file", 
            filetypes=(("JavaScript files", ".js"), ("All Files", "*.*"))
        )

        js_file = open(root.filename)
        lines = js_file.readlines()

        return lines