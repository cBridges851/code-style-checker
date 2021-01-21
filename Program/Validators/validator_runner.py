from Validators.conditional_statement_signature_quantity_on_line_validator import ConditionalStatementSignatureQuantityOnLineValidator
from Validators.loop_signature_quantity_on_line_validator import LoopSignatureQuantityOnLineValidator
from Validators.end_of_signature_space_validator import EndOfSignatureSpaceValidator
from Validators.equals_space_missing_validator import EqualsSpaceMissingValidator
from Validators.number_of_classes_validator import NumberOfClassesValidator
from Validators.start_of_signature_spaceValidator import StartOfSignatureSpaceValidator
from Validators.var_use_validator import VarUseValidator


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
            ConditionalStatementSignatureQuantityOnLineValidator(),
            LoopSignatureQuantityOnLineValidator(),
            EqualsSpaceMissingValidator(),
            NumberOfClassesValidator(),
            VarUseValidator(),
            StartOfSignatureSpaceValidator(),
            EndOfSignatureSpaceValidator()
        ]

        # Calls each validator and runs them
        for validator in validators:
            validator_results = validator.validate(code_box_lines)
            # Add the results of each individual validator to the whole one
            error_dictionary["error_list"].append(validator_results["error_list"])
            error_dictionary["error_count"] += validator_results["error_count"]

        return(error_dictionary)