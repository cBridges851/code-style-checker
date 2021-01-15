import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from Validators.ValidatorRunner import ValidatorRunner

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

    def clear_code_box(self):
        """
            Removes placeholder text from the box where the user inputs their code.
            Args:
                code_box: ScrolledText, the box where the user inputs their code.
        """
        if self.code_box.get("1.0", tk.END) == "Input JavaScript Code Here...\n":
            self.code_box.delete("1.0", tk.END)

    def insert_placeholder(self):
        """
            Puts in the placeholder if there is nothing in the box.
            Args:
                code_box: ScrolledText, the box where the user inputs their code.
        """
        if self.code_box.get("1.0", tk.END) == "\n":
            self.code_box.insert(tk.END, "Input JavaScript Code Here...")
    
    def output_results(self):
        # Allow the output box to be edited
        self.output_box.configure(state="normal")
        self.output_box.delete("1.0", tk.END)
        code_box_text = self.code_box.get("1.0", tk.END)
        code_box_lines = code_box_text.split("\n")
        validator_results = ValidatorRunner().run_validators(code_box_lines)

        if validator_results["error_count"] == 0:
            # No errors
            self.output_box.configure(bg="#004512")
            self.output_box.insert(tk.END, "There are no style errors in the code!")
        else:
            # 1 or more errors
            self.output_box.configure(bg="#450000")

            if validator_results["error_count"] == 1:
                starting_error_message = "There is 1 style error in this code: \n\n"
            else:
                starting_error_message = f"There are {validator_results['error_count']} style errors in this code: \n\n"
            
            self.output_box.insert(tk.END, starting_error_message)

            for category in validator_results["error_list"]:
                for error in category:
                    self.output_box.insert(tk.END, f"{error}\n")
                
                if len(category) != 0:
                    self.output_box.insert(tk.END, "\n")

        # User cannot edit the output box after the message has been inserted
        self.output_box.configure(state="disabled")

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

    def render_code_input_box(self):
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
        self.insert_placeholder()
        self.code_box.bind(
            "<Button 1>", 
            lambda event: self.clear_code_box()
        )
        self.code_box.bind(
            "<FocusOut>", 
            lambda event: self.insert_placeholder()
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
            command= self.output_results
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
        self.render_title()
        self.render_code_input_box()
        self.render_validate_button()
        self.render_output_box()
        self.root.mainloop()
