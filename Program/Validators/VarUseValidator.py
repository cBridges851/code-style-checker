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
                error_list: list, all of the errors that have been found for 
                                    this validator.
        """
        error_list = []
        var_regex = "var\\b"

        for line in lines:
            if len(re.findall(var_regex, line)) != 0:
                if len(re.findall(var_regex, line)) == 1:
                    error_list.append("Var Error: 1 occurrence of the use of var on line" 
                    + f" {lines.index(line) + 1}. Use let or const.")
                else:
                    error_list.append(f"Var Error: {len(re.findall(var_regex, line))}"
                    + " occurrences of the use of var on line" 
                    + f" {lines.index(line) + 1}. Use let or const.")

        return error_list