import re


class ConditionalStatementQuantityOnLineValidator:
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
        conditional_statement_regex = r"(if|else if|else)"

        for line in lines:
            line_number += 1

            # Makes sure there is only one conditional statement keyword on a line
            if len(re.findall(conditional_statement_regex, line)) > 1:
                error_dictionary["error_list"] \
                    .append("Conditional Statement On Line Quantity Error:"
                            + " There are too many conditional statement"
                            + f" signatures on line {line_number}")
                error_dictionary["error_count"] += 1

        return error_dictionary