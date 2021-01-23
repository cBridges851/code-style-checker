import re


class VarUseValidator:
    """
        The validator that is used to check for occurrences of 'var'.
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

        # Regex that looks for "var"
        var_regex = r"var\b"
        # Initial line number
        line_number = 0

        # Loops through every line in the code
        for line in lines:
            # Increments the line the user is on
            line_number += 1

            # If there are occurrence of var on the line
            if len(re.findall(var_regex, line)) != 0:
                # Checks the number of occurrence to enable a gramattically correct output
                if len(re.findall(var_regex, line)) == 1:
                    # Appends an error with the line number and increments the count
                    error_dictionary["error_list"] \
                        .append("Var Error: 1 occurrence of the use of var on line"
                                + f" {line_number}. Use let or const.")
                    error_dictionary["error_count"] += 1
                else:
                    # Appends an error with the number of vars on the line, 
                    # and increments the count by this number
                    error_dictionary["error_list"] \
                        .append(f"Var Error: {len(re.findall(var_regex, line))}"
                                + " occurrences of the use of var on line"
                                + f" {line_number}. Use let or const.")
                    error_dictionary["error_count"] += len(re.findall(var_regex, line))

        # Returns the lines and the number of errors after all the lines have been checked
        return error_dictionary