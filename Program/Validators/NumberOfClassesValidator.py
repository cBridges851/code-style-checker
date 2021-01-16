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
        
        class_regex = "class\\b"
        line_number = 0
        number_of_classes = 0

        for line in lines:
            line_number += 1

            if len(re.findall(class_regex, line)) != 0:
                number_of_classes += 1

                if number_of_classes > 1:
                    error_dictionary["error_count"] += 1
                    error_dictionary["error_list"] \
                    .append("Class Quantity Error: Move the class starting"
                    + f" on line {line_number} to its own file.")
        
        return error_dictionary