import re


class EndOfSignatureSpaceValidator:
    """
        The validator that is used to check that there is a space between a 
        word or ) and {.
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

        bracket_end_regex = r"[a-zA-Z0-9\=\( ]+\){"
        word_ending_regex = r"[A-Za-z]+{"
        line_number = 0

        for line in lines:
            # Check signatures with a )
            bracket_end_on_line = re.findall(bracket_end_regex, line)
            # Check else signatures
            word_end_on_line = re.findall(word_ending_regex, line)
            line_number += 1
            
            # Check signatures with a ) first
            if len(bracket_end_on_line) != 0:
                for bracket_end_entry in bracket_end_on_line:
                    error_dictionary["error_list"] \
                        .append("End Of Signature Error: A space is needed in"
                                + f" '{bracket_end_entry.strip()}'" 
                                + " between the ) and {" 
                                + f" on line {line_number}.")
                    error_dictionary["error_count"] += 1

            # Then check signatures with an else
            if len(word_end_on_line) != 0:
                for word_end_entry in word_end_on_line:
                    error_dictionary["error_list"] \
                        .append("End Of Signature Error: A space is needed"
                                + " between the word and {"
                                + f" in '{word_end_entry}'")

                error_dictionary["error_count"] += len(word_end_on_line)

        return error_dictionary