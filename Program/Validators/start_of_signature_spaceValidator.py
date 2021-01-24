import re


class StartOfSignatureSpaceValidator:
    """
        The validator that is used to check that there is a space between a while/for,
        if/else if/switch and ()
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

        # Looks for "while" or "for"
        loop_start_regex = r"(while|for)\("
        # Looks for "if", "else if" or "switch"
        conditional_start_regex = r"(if|else if|switch)\("
        # Initial line number
        line_number = 0

        # Loops through every line in the code
        for line in lines:
            # Check loop signatures
            loop_space_lack_on_line = re.findall(loop_start_regex, line)
            # Check conditional statement signatures
            conditional_space_lack_on_line = re.findall(conditional_start_regex, line)
            # Increments the line the user is on
            line_number += 1

            # Check loop signatures first
            if len(loop_space_lack_on_line) != 0:
                # Calls a function in this file to check the loop signatures
                self.add_error(loop_space_lack_on_line, line_number, error_dictionary)

            # Then check conditional statement signatures
            if len(conditional_space_lack_on_line) != 0:
                # Calls a function in this file to check the conditional statement signatures
                self.add_error(conditional_space_lack_on_line, line_number, error_dictionary)

        # Returns the lines and the number of errors after all the lines have been checked
        return error_dictionary

    def add_error(self, signature_errors, line_number, error_dictionary):
        # Loops through all the errors for the type of signature
        for error in signature_errors:
            # Appends each error along with the line number, and the count is incremented
            error_dictionary["error_list"] \
                .append("Start Of Signature Error: A space is needed"
                        + f" after the {error}"
                        + f" on line {line_number}.")
            error_dictionary["error_count"] += 1