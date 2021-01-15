from Validators.EqualsSpaceMissingValidator import EqualsSpaceMissingValidator
from Validators.VarUseValidator import VarUseValidator

class ValidatorRunner:
    """
        The class that is responsible for running all the validators.
    """
    def run_validators(self, code_box_lines):
        """
            Runs the validators.
            Args: 
                code_box_lines: list, all the lines that are in the box 
                                    where the user inputs code.
            Returns:
                error_dictionary: dictionary, contains the errors and 
                                    how many there are.
        """
        error_dictionary = {
            "error_list": [],
            "error_count": 0
        }
        validators = [
            EqualsSpaceMissingValidator(),
            VarUseValidator()
        ]

        for validator in validators:
            validator_results = validator.validate(code_box_lines)
            error_dictionary["error_list"].append(validator_results["error_list"])
            error_dictionary["error_count"] += validator_results["error_count"]

        return(error_dictionary)