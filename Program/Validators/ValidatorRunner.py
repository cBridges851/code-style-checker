from Validators.EqualsSpaceMissingValidator import EqualsSpaceMissingValidator
from Validators.VarUseValidator import VarUseValidator

class ValidatorRunner:
    def run_validators(self, code_box_lines):
        error_dictionary = {
            "errors": [],
            "error_count": 0
        }
        validators = [
            EqualsSpaceMissingValidator(),
            VarUseValidator()
        ]

        for validator in validators:
            validator_results = validator.validate(code_box_lines)
            error_dictionary["errors"].append(validator_results)
            error_dictionary["error_count"] += len(validator_results)


        return(error_dictionary)