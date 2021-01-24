import re


class LoopSignatureQuantityOnLineValidator:
    """
        The validator that is used to check that there is no more than one
        loop signature on a line
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

        # Regex that looks for "while" or "for" 
        loop_regex = r"(while|for)"
        # Initial line number
        line_number = 0

        # Loops through every line in the code
        for line in lines:
            # Increments the line the user is on
            line_number += 1

            # Makes sure there is only one conditional statement keyword on a line
            if len(re.findall(loop_regex, line)) > 1:
                # Appends an error if there are too many conditional statement
                # keywords on a line and increments the count
                error_dictionary["error_list"] \
                    .append("Loop Signatures On Line Quantity Error:"
                            + " There are too many loop"
                            + f" signatures on line {line_number}")
                error_dictionary["error_count"] += 1

        # Returns the lines and the number of errors after all the lines have been checked
        return error_dictionary
