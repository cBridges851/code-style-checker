import re


class ConditionalStatementSignatureQuantityOnLineValidator:
    """
        The validator that is used to check that there is
        no more than one conditional statement signature on a line.
    """

    def validate(self, lines):
        """
            The method that validates the code.
            Args:
                lines: list, all the lines of code to check
            Returns:
                error_dictionary: dictionary, all of the errors that have been found for
                this validator and how many.
        """

        # Initial value for the error dictionary
        error_dictionary = {
            "error_list": [],
            "error_count": 0
        }

        # Initial line number
        line_number = 0
        # Looks for the if, else if, and else keywords
        conditional_statement_regex = r"(if|else if|else)"

        # Loops through every line in the code
        for line in lines:
            # Increments the line number the user is on
            line_number += 1

            # Makes sure there is only one conditional statement keyword on a line
            if len(re.findall(conditional_statement_regex, line)) > 1:
                # Adds an error if there is more than one conditional statement keyword on a line
                error_dictionary["error_list"] \
                    .append("Conditional Statement Signatures On Line Quantity Error:"
                            + " There are too many conditional statement"
                            + f" signatures on line {line_number}")
                error_dictionary["error_count"] += 1

        # Returns the lines and the number of errors after all the lines have been checked
        return error_dictionary