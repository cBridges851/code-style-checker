import re


class LoopSignatureQuantityOnLineValidator:
    """
        The validator that is used to check that there is one
        if statement on a line
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

        error_dictionary = {
            "error_list": [],
            "error_count": 0
        }

        line_number = 0
        loop_regex = r"(while|for)"

        for line in lines:
            line_number += 1

            # Makes sure there is only one conditional statement keyword on a line
            if len(re.findall(loop_regex, line)) > 1:
                error_dictionary["error_list"] \
                    .append("Loop Signature On Line Quantity Error:"
                            + " There are too many loop"
                            + f" signatures on line {line_number}")
                error_dictionary["error_count"] += 1

        return error_dictionary