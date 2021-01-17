from Validators.EndOfSignatureSpaceValidator import EndOfSignatureSpaceValidator
from Validators.EqualsSpaceMissingValidator import EqualsSpaceMissingValidator
from Validators.NumberOfClassesValidator import NumberOfClassesValidator
from Validators.StartOfSignatureSpaceValidator import StartOfSignatureSpaceValidator
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

        # List of all the validators
        validators = [
            EndOfSignatureSpaceValidator(),
            EqualsSpaceMissingValidator(),
            NumberOfClassesValidator(),
            StartOfSignatureSpaceValidator(),
            VarUseValidator()
        ]

        # Calls each validator and runs them
        for validator in validators:
            validator_results = validator.validate(code_box_lines)
            # Add the results of each individual validator to the whole one
            error_dictionary["error_list"].append(validator_results["error_list"])
            error_dictionary["error_count"] += validator_results["error_count"]

        return(error_dictionary)