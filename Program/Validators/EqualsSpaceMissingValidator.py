import re

class EqualsSpaceMissingValidator:
    """
        The validator that is used to check for missing spaces on the left 
        and right of equals signs.
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

        for line in lines:
            if len(re.findall("[^ =]=", line)) != 0:
                for occurence in re.findall("[^ =]=", line):
                    error_list.append(f"Equals Sign Space Missing Error: {occurence}"
                    + f" on line {lines.index(line) + 1} needs a space on the left of the =.")

            if len(re.findall("=[^ =]", line)) != 0:
                for occurence in re.findall("=[^ =]", line):
                    error_list.append(f"Equals Sign Space Missing Error: {occurence}"
                    + f" on line {lines.index(line) + 1} needs a space on the right of the =.")

        return error_list