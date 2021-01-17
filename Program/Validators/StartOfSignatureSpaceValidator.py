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

        loop_start_regex = r"(while|for)\("
        conditional_start_regex = r"(if|else if|switch)\("