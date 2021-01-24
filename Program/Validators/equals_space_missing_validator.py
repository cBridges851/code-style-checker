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
                error_dictionary: dictionary, all of the errors that have been found for
                this validator and how many.
        """

        # Initial value for the error dictionary
        error_dictionary = {
            "error_list": [],
            "error_count": 0
        }

        # Regex that checks for a lack of a space on the left of an equals sign 
        # (unless it is another operator for mathematical operations or comparisons)
        left_space_regex = r"[^ \+\-\*\/\!=]="
        # Regex that checks for a lack of a space on the right of an equals sign 
        # (unless it is another equals sign for ==)
        right_space_regex = r"=[^ =]"
        # Initial line number
        line_number = 0

        # Loops through every line in the code
        for line in lines:
            # Increments the line the user is on
            line_number += 1

            # Check for missing space on the left of = occurrences on a line
            if len(re.findall(left_space_regex, line)) != 0:
                # Appends an error for each occurrence on the line
                for occurrence in re.findall(left_space_regex, line):
                    error_dictionary["error_list"] \
                    .append(f"Equals Sign Space Missing Error: {occurrence}"
                            + f" on line {line_number} needs a"
                            + " space on the left of the =.")

                # Adds the number of occurrences on a line to the count
                error_dictionary["error_count"] += len(re.findall(left_space_regex, line))

            # Check for missing space on the right of =
            if len(re.findall(right_space_regex, line)) != 0:
                # Appends an error for each occurrence on the line
                for occurence in re.findall(right_space_regex, line):
                    error_dictionary["error_list"] \
                    .append(f"Equals Sign Space Missing Error: {occurence}"
                            + f" on line {line_number} needs a space on the right of the =.")

                # Adds the number of occurrences on a line to the count
                error_dictionary["error_count"] += len(re.findall(right_space_regex, line))

        # Returns the lines and the number of errors after all the lines have been checked
        return error_dictionary