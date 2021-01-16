import re


class EndOfSignatureSpaceValidator:
    """
        The validator that is used to check for occurrences of 'var'.
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

        signature_end_regex = r"[a-zA-Z0-9\=\( ]+\){"
        else_regex = r"else{"
        line_number = 0

        for line in lines:
            # Check signatures with a )
            signatures_on_line = re.findall(signature_end_regex, line)
            # Check else signatures
            else_on_line = re.findall(else_regex, line)
            line_number += 1
            
            # Check signatures with a ) first
            if len(signatures_on_line) != 0:
                for signature in signatures_on_line:
                    error_dictionary["error_list"] \
                        .append("End Of Signature Error: A space is needed in"
                                + f" '{signature.strip()}'" 
                                + " between the ) and {.")
                    error_dictionary["error_count"] += 1

            # Then check signatures with an else
            if len(else_on_line) != 0:
                if len(else_on_line) == 1:
                    error_dictionary["error_list"] \
                        .append("End Of Signature Error: A space is needed"
                                + " between the else and {"
                                + f" in 1 place on line {line_number}")
                else:
                    error_dictionary["error_list"] \
                        .append("End Of Signature Error: A space is needed"
                                + " between the else and {"
                                + f" in {len(else_on_line)} places on line {line_number}")

                error_dictionary["error_count"] += len(else_on_line)

        return error_dictionary