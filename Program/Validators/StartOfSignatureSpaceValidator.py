import re


class StartOfSignatureSpaceValidator:
    """
        The validator that is used to check that there is a space between a while/for,
        if/else if/else and ()
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

        loop_start_regex = r"(while|for)\("
        conditional_start_regex = r"(if|else if|switch)\("
        line_number = 0

        for line in lines:
            # Check loop signatures
            loop_space_lack_on_line = re.findall(loop_start_regex, line)
            # Check conditional statement signatures
            conditional_space_lack_on_line = re.findall(conditional_start_regex, line)
            line_number += 1

            # Check loop signatures first
            if len(loop_space_lack_on_line) != 0:
                self.add_error(loop_space_lack_on_line, line_number, error_dictionary)

            # Then check conditional statement signatures
            if len(conditional_space_lack_on_line) != 0:
                self.add_error(conditional_space_lack_on_line, line_number, error_dictionary)

        return error_dictionary

    def add_error(self, signature_errors, line_number, error_dictionary):
        for error in signature_errors:
            error_dictionary["error_list"] \
                .append("Start Of Signature Error: A space is needed"
                        + f" after the {error}"
                        + f" on line {line_number}.")
            error_dictionary["error_count"] += 1