import tkinter as tk
from View.comment_remover import CommentRemover
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
        # Delete the previous contents in the output box
        output_box.delete("1.0", tk.END)
        # Gets the code in the input box
        code_box_text = code_box.get("1.0", tk.END)
        # Splits the code so it is a list of each line
        code_box_lines = code_box_text.split("\n")
        # Calls a function to remove any comments and return the lines back
        code_box_lines = CommentRemover().remove_comments(code_box_lines)
        # Calls validates the lines and stores the results
        validator_results = ValidatorRunner().run_validators(code_box_lines)

        if validator_results["error_count"] == 0:
            # No errors
            output_box.configure(bg="#004512")  # Green background
            output_box.insert(tk.END, "There are no style errors in the code!")
        else:
            # 1 or more errors
            output_box.configure(bg="#450000")  # Red background

            # Checks number of errors so correct grammar can be used, so the starting error message is created
            if validator_results["error_count"] == 1:
                starting_error_message = "There is 1 style error in this code: \n\n"
            else:
                starting_error_message = f"There are {validator_results['error_count']} style errors in this code: \n\n"

            # Puts the starting error message in the output box
            output_box.insert(tk.END, starting_error_message)

            # Loops through each list of errors inside the overall error list
            for category in validator_results["error_list"]:
                for error in category:
                    # Outputs the error
                    output_box.insert(tk.END, f"{error}\n")

                # Insert a new line if there are values in the category
                if len(category) != 0:
                    output_box.insert(tk.END, "\n")

        # User cannot edit the output box after the message has been inserted
        output_box.configure(state="disabled")