import re

class EqualsSpaceMissingValidator:
    def validate(self, lines):
        error_list = []

        for line in lines:
            if len(re.findall("[^ =]=", line)) != 0:
                for occurence in re.findall("[^ =]=", line):
                    error_list.append(f"Equals Sign Space Missing Error: {occurence}"
                    + f" on line {lines.index(line) + 1} needs a space on the left of the =.")

            if len(re.findall("=[^ =]", line)) != 0:
                for occurence in re.findall("=[^ =]", line):
                    error_list.append(f"Equals Sign Space Missing Error: {occurence}"
                    + f" on line {lines.index(line) + 1} needs a space on the right of the =.")

        return error_list