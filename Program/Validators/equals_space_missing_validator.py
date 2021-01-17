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

        error_dictionary = {
            "error_list": [],
            "error_count": 0
        }

        line_number = 0
        left_space_regex = r"[^ =]="
        right_space_regex = r"=[^ =]"

        for line in lines:
            line_number += 1

            # Check for missing space on the left of =
            if len(re.findall(left_space_regex, line)) != 0:
                error_dictionary["error_count"] += len(re.findall(left_space_regex, line))

                for occurrence in re.findall(left_space_regex, line):
                    error_dictionary["error_list"] \
                    .append(f"Equals Sign Space Missing Error: {occurrence}"
                            + f" on line {line_number} needs a"
                            + " space on the left of the =.")

            # Check for missing space on the right of =
            if len(re.findall(right_space_regex, line)) != 0:
                error_dictionary["error_count"] += len(re.findall(right_space_regex, line))

                for occurence in re.findall(right_space_regex, line):
                    error_dictionary["error_list"] \
                    .append(f"Equals Sign Space Missing Error: {occurence}"
                            + f" on line {line_number} needs a space on the right of the =.")

        return error_dictionary