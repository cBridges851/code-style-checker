import re

class VarUseValidator:
    def validate(self, lines):
        error_list = []
        var_regex = "var\\b"

        for line in lines:
            if len(re.findall(var_regex, line)) != 0:
                if len(re.findall(var_regex, line)) == 1:
                    error_list.append("Var Error: 1 occurrence of the use of var on line" 
                    + f" {lines.index(line)}. Use let or const.")
                else:
                    error_list.append(f"Var Error: {len(re.findall(var_regex, line))}"
                    + " occurrences of the use of var on line" 
                    + f" {lines.index(line)}. Use let or const.")

        return error_list