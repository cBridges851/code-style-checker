import re

class OperatorSpacingValidator:
    def validate(self, lines):
        error_list = []
        for line in lines:
            if len(re.findall("[^ =]=", line)) != 0:
                for occurence in re.findall("[^ =]=", line):
                    error_list.append(f"Operator Spacing Error: {occurence}"
                    + f" on line {lines.index(line)} needs a space on the left of the =.")

            if len(re.findall("=[^ =]", line)) != 0:
                for occurence in re.findall("[^ =]=", line):
                    error_list.append(f"Operator Spacing Error: {occurence}"
                    + f" on line {lines.index(line)} needs a space on the right of the =.")

        return error_list