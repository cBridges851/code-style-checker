import tkinter as tk
from Validators.validator_runner import ValidatorRunner

class Outputter:
    """
        The class that is responsible for outputting results.
    """
    
    def output_results(self, code_box, output_box):
        """
            Outputs the results of the validators onto the output box.
        """
        # Allow the output box to be edited
        output_box.configure(state="normal")
        output_box.delete("1.0", tk.END)
        code_box_text = code_box.get("1.0", tk.END)
        code_box_lines = code_box_text.split("\n")
        validator_results = ValidatorRunner().run_validators(code_box_lines)

        if validator_results["error_count"] == 0:
            # No errors
            output_box.configure(bg="#004512")
            output_box.insert(tk.END, "There are no style errors in the code!")
        else:
            # 1 or more errors
            output_box.configure(bg="#450000")

            # Checks number of errors so correct grammar can be used
            if validator_results["error_count"] == 1:
                starting_error_message = "There is 1 style error in this code: \n\n"
            else:
                starting_error_message = f"There are {validator_results['error_count']} style errors in this code: \n\n"

            output_box.insert(tk.END, starting_error_message)

            for category in validator_results["error_list"]:
                for error in category:
                    output_box.insert(tk.END, f"{error}\n")

                # Insert a new line if there are values in the category
                if len(category) != 0:
                    output_box.insert(tk.END, "\n")

        # User cannot edit the output box after the message has been inserted
        output_box.configure(state="disabled")