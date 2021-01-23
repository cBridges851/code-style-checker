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

        # Initial value for the error dictionary
        error_dictionary = {
            "error_list": [],
            "error_count": 0
        }

        # Looks for the name of the class, but does not include the word
        # "class" in the result
        class_regex = r"(?<=class )[A-Za-z0-9]+"
        number_of_classes = 0
        # Initial line number
        line_number = 0

        # Loops through every line in the code
        for line in lines:
            # Looks for classes on the line
            classes_on_line = re.findall(class_regex, line)
            # Increments the line the user is on
            line_number += 1

            # If there is at least one class on a line
            if len(classes_on_line) != 0:
                number_of_classes += 1

                if len(classes_on_line) == 1:
                    # For if there is one class on a line
                    if number_of_classes > 1:
                        # Append an error if the number of classes in the 
                        # file is greater than 1 and increments the count
                        error_dictionary["error_list"] \
                            .append(f"Class Quantity Error: Move the"
                                    + f" {classes_on_line[0]} class"
                                    + " to its own file.")
                        error_dictionary["error_count"] += 1
                else:
                    # For when someone makes multiple classes on a line
                    for i in range(1, len(classes_on_line)):
                        # Loops through each class after the first one and 
                        # appends an error for each occurrence after this
                        error_dictionary["error_list"] \
                            .append(f"Class Quantity Error: Move the"
                                    + f" {classes_on_line[i]} class"
                                    + " to its own file.")

                    # Add the number of classes, but subtracts 1 to eliminate the first
                    error_dictionary["error_count"] += len(classes_on_line) - 1

        # Returns the lines and the number of errors after all the lines have been checked
        return error_dictionary