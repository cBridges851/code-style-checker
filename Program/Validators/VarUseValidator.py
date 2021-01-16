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
        error_dictionary = {
            "error_list": [],
            "error_count": 0
        }

        var_regex = r"var\b"
        line_number = 0

        for line in lines:
            line_number += 1

            # If there are occurrence of var on the line
            if len(re.findall(var_regex, line)) != 0:
                # Checks the number of occurrence to enable a gramattically correct output
                if len(re.findall(var_regex, line)) == 1:
                    error_dictionary["error_list"] \
                        .append("Var Error: 1 occurrence of the use of var on line"
                                + f" {line_number}. Use let or const.")
                    error_dictionary["error_count"] += 1
                else:
                    error_dictionary["error_list"] \
                        .append(f"Var Error: {len(re.findall(var_regex, line))}"
                                + " occurrences of the use of var on line"
                                + f" {line_number}. Use let or const.")
                    error_dictionary["error_count"] += len(re.findall(var_regex, line))

        return error_dictionary