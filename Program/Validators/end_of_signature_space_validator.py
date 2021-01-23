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

        # Initial value for the error dictionary
        error_dictionary = {
            "error_list": [],
            "error_count": 0
        }

        # Regex that checks for a lack of space between a ) and {
        bracket_end_regex = r"[a-zA-Z0-9\=\( ]+\){"
        # Regexg that checks for a lack of space between a word and {
        word_ending_regex = r"[A-Za-z]+{"
        # Initial line number
        line_number = 0

        for line in lines:
            # Check signatures with a )
            bracket_end_on_line = re.findall(bracket_end_regex, line)
            # Check else signatures
            word_end_on_line = re.findall(word_ending_regex, line)
            # Increments the line the user is on
            line_number += 1
            
            # Check signatures with a ) first
            if len(bracket_end_on_line) != 0:
                # Loops through the number of occurrences of a lack of a space between a (
                # and { on a line and adds an error to the dictionary for each occurrence
                for bracket_end_entry in bracket_end_on_line:
                    error_dictionary["error_list"] \
                        .append("End Of Signature Error: A space is needed in"
                                + f" '{bracket_end_entry.strip()}'" 
                                + " between the ) and {" 
                                + f" on line {line_number}.")
                    
                    # Adds the number of occurrences on a line to the error count
                    error_dictionary["error_count"] += 1

            # Then check signatures with an else
            if len(word_end_on_line) != 0:
                # Loops through the number of occurrences of a lack of a space between a word
                # and { on a line and adds an error to the dictionary for each occurrence
                for word_end_entry in word_end_on_line:
                    error_dictionary["error_list"] \
                        .append("End Of Signature Error: A space is needed"
                                + " between the word and {"
                                + f" in '{word_end_entry}'")

                # Adds the number of occurrences to the error count
                error_dictionary["error_count"] += len(word_end_on_line)

        # Returns the lines and the number of errors after all the lines have been checked
        return error_dictionary