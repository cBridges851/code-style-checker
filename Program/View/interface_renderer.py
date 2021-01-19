import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from View.code_box_manager import CodeBoxManager
from View.outputter import Outputter


class InterfaceRenderer:
    """
        Renders the user interface and displays it.
    """

    def __init__(self):
        """
            Initialises the InterfaceRenderer class. It sets up the root and defines
            variables used in multiple places in the rendering.
        """
        self.root = tk.Tk()
        self.title_label = tk.Label(self.root)
        self.code_box = ScrolledText(self.root)
        self.validate_button = tk.Button(self.root)
        self.output_box = ScrolledText(self.root)
        self.primary_bg_colour = "#1D1D1D"
        self.secondary_bg_colour = "#2D2D2D"
        self.box_font_colour = "#C2C0C0"
        self.box_width = 50
        self.box_font = ("Consolas 14")

    def render_window(self):
        """
            Creates the root window for the application.
        """
        self.root.iconbitmap("view/favicon.ico")
        self.root.title("Chrispy Code Style Checker")
        self.root.resizable(False, False)
        self.root.configure(
            bg=self.primary_bg_colour,
            padx=10,
            pady=10
        )

    def render_menu_bar(self):
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(
            label="Open File",
            command=lambda: CodeBoxManager().display_file_contents(self.root, self.code_box))
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menu_bar)

    def render_title(self):
        """
            Creates the title of the application.
        """
        self.title_label.configure(
            text="Chrispy Code Style Checker",
            bg=self.primary_bg_colour,
            fg="#FFFFFF",
            font=("Helvetica 26 bold")
        )
        self.title_label.grid(row=0, column=0)

    def render_code_box(self):
        """
            Creates the box that will be used to input code.
        """
        self.code_box.configure(
            width=self.box_width,
            height=15,
            bg=self.secondary_bg_colour,
            fg=self.box_font_colour,
            font=self.box_font
        )
        CodeBoxManager().insert_placeholder(self.root, self.code_box)

        # Event for when the box is clicked on
        self.code_box.bind(
            "<Button 1>",
            lambda event: CodeBoxManager().clear_code_box(self.code_box)
        )

        # Event for when the box does not have a focus on it
        self.code_box.bind(
            "<FocusOut>",
            lambda event: CodeBoxManager().insert_placeholder(self.root, self.code_box)
        )
        self.code_box.grid(row=1, column=0)

    def render_validate_button(self):
        """
            Creates the button that will trigger the code to be validated.
        """
        self.validate_button.configure(
            text="VALIDATE!",
            width=41,
            font=("Helvetica 14"),
            bg="#7A7A7A",
            command=lambda: Outputter().output_results(self.code_box, self.output_box)
        )
        self.validate_button.grid(row=2, column=0, pady=10)

    def render_output_box(self):
        """
            Creates the box that will be used to display the output.
        """
        self.output_box.configure(
            width=self.box_width,
            height=7,
            bg=self.secondary_bg_colour,
            fg=self.box_font_colour,
            state="disabled",
            font=self.box_font,
            wrap="word"
        )
        self.output_box.grid(row=3, column=0)

    def render_interface(self):
        """
            Generates the entire user interface by calling all the methods
            that build up each component.
        """
        self.render_window()
        self.render_menu_bar()
        self.render_title()
        self.render_code_box()
        self.render_validate_button()
        self.render_output_box()
        self.root.mainloop()
