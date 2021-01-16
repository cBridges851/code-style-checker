import re


class NumberOfClassesValidator:
    """
        The validator that is used to check how many classes are present in the file.
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

        class_regex = r"(?<=class )[A-Za-z]+"
        line_number = 0
        number_of_classes = 0

        for line in lines:
            classes_on_line = re.findall(class_regex, line)
            line_number += 1

            # If there is at least one class on a line
            if len(classes_on_line) != 0:
                number_of_classes += 1

                if len(classes_on_line) == 1:
                    if number_of_classes > 1:
                        error_dictionary["error_count"] += 1
                        error_dictionary["error_list"] \
                            .append(f"Class Quantity Error: Move the"
                                    + f" {classes_on_line[0]} class"
                                    + " to its own file.")
                else:
                    # For when someone makes multiple classes on a line
                    for i in range(1, len(classes_on_line)):
                        error_dictionary["error_list"] \
                            .append(f"Class Quantity Error: Move the"
                                    + f" {classes_on_line[i]} class"
                                    + " to its own file.")

                    error_dictionary["error_count"] += len(classes_on_line) - 1

        return error_dictionary