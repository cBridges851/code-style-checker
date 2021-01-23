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
        # Initialises the root of the program
        self.root = tk.Tk()
        # Initialises the title label for the program
        self.title_label = tk.Label(self.root)
        # Initialises the box where the user will input code
        self.code_box = ScrolledText(self.root)
        # Initialise the validate button
        self.validate_button = tk.Button(self.root)
        # Initialise the box where the results will be outputted
        self.output_box = ScrolledText(self.root)
        # Initialises the menu bar
        self.menu_bar = tk.Menu(self.root)
        # Initialises the menu that will be in the menu bar
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        # Sets the main background colour
        self.primary_bg_colour = "#1D1D1D"
        # Sets the second background colour
        self.secondary_bg_colour = "#2D2D2D"
        # Sets the colour of the text
        self.box_font_colour = "#C2C0C0"
        # Sets the width the boxes need to be
        self.box_width = 50
        # Sets the font and its size for text in the boxes
        self.box_font = ("Consolas 14")

    def render_window(self):
        """
            Creates the root window for the application.
        """
        # Sets the icon window
        self.root.iconbitmap("view/favicon.ico")
        # Sets the title for the application
        self.root.title("Chrispy Code Style Checker")
        # Makes the window not resizable
        self.root.resizable(False, False)
        # Add a background colour to the root and padding on x and y axes
        self.root.configure(
            bg=self.primary_bg_colour,
            padx=10,
            pady=10
        )

    def render_menu_bar(self):
        # Adds the open file option in the menu
        self.file_menu.add_command(
            label="Open File",
            command=lambda: CodeBoxManager().display_file_contents(self.root, self.code_box))  # Calls a function that opens the file dialogs
        # Add the exit option in the menu which will allow the user to close the program
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        # Adds the group for opening the file and exiting
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        # Assigns the menu bar as the root's menu
        self.root.config(menu=self.menu_bar)

    def render_title(self):
        """
            Creates the title of the application.
        """
        # Style the title
        self.title_label.configure(
            text="Chrispy Code Style Checker",
            bg=self.primary_bg_colour,
            fg="#FFFFFF",
            font=("Helvetica 26 bold")
        )
        # Put the title on the window
        self.title_label.grid(row=0, column=0)

    def render_code_box(self):
        """
            Creates the box that will be used to input code.
        """
        # Style the code input box
        self.code_box.configure(
            width=self.box_width,
            height=15,
            bg=self.secondary_bg_colour,
            fg=self.box_font_colour,
            font=self.box_font
        )
        # Put the placeholder in the box
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
        # Put the code input box on the window
        self.code_box.grid(row=1, column=0)

    def render_validate_button(self):
        """
            Creates the button that will trigger the code to be validated.
        """
        # Style the validate button
        self.validate_button.configure(
            text="VALIDATE!",
            width=41,
            font=("Helvetica 14"),
            bg="#7A7A7A",
            command=lambda: Outputter().output_results(self.code_box, self.output_box)  # Triggers the results to be outputted when pressed 
        )
        # Put the validate button on the window
        self.validate_button.grid(row=2, column=0, pady=10)

    def render_output_box(self):
        """
            Creates the box that will be used to display the output.
        """
        # Style the output box
        self.output_box.configure(
            width=self.box_width,
            height=7,
            bg=self.secondary_bg_colour,
            fg=self.box_font_colour,
            state="disabled",
            font=self.box_font,
            wrap="word"
        )
        # Put the output box on the window
        self.output_box.grid(row=3, column=0)

    def render_interface(self):
        """
            Generates the entire user interface by calling all the methods
            that build up each component.
        """
        # Builds the window
        self.render_window()
        # Builds the menu bar
        self.render_menu_bar()
        # Builds the title
        self.render_title()
        # Builds the code input box
        self.render_code_box()
        # Builds the validate button
        self.render_validate_button()
        # Builds the output box 
        self.render_output_box()
        # Loops the application
        self.root.mainloop()
