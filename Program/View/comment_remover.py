import re


class CommentRemover:
    """
        The class that is responsible for removing comments in the lines
        so they are not part of the validation.
    """

    def remove_comments(self, original_lines):
        """
            The method that removes the comments.
            Args:
                original_lines: list, the list of lines that is the entirity 
                of the inputted code.
        """
        lines_without_comments = []
        # Remove single line comments
        for line in original_lines:
            comment = re.findall("//.+", line)
            if len(comment) != 0:
                line = line.replace(comment[0], "")
            lines_without_comments.append(line)

        return lines_without_comments

CommentRemover().remove_comments(["let x = 0; // The program", "console.log('Hello')"])
