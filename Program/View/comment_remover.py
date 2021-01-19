import re


class CommentRemover:
    """
        The class that is responsible for removing comments in the lines
        so they are not part of the validation.
    """

    def remove_comments(self, lines):
        """
            The method that removes the comments.
            Args:
                lines: list, the list of lines that is the entirity 
                of the inputted code.
            Returns:
                lines: list, the list of lines with the comments removed.
        """
        
        is_multiline_comment = False

        # Remove single line comments
        for i in range(len(lines)):
            single_line_comment = re.findall(r"//.+", lines[i])
            multiline_comment_start = re.findall(r"/\*(.+)?", lines[i])
            multiline_comment_finish = re.findall(r"(.+)?\*/", lines[i])

            # Removes single line comments
            if len(single_line_comment) != 0:
                lines[i] = lines[i].replace(single_line_comment[0], "")
            
            # Remove multiline comments
            if not is_multiline_comment:
                # Check if multiline started
                if len(multiline_comment_start) != 0:
                    lines[i] = lines[i].replace(multiline_comment_start[0], "")
                    is_multiline_comment = True
            
                if len(multiline_comment_finish) != 0:
                    lines[i] = lines[i].replace(multiline_comment_finish[0], "")
                    is_multiline_comment = False
            else:
                if len(multiline_comment_finish) != 0:
                    lines[i] = lines[i].replace(multiline_comment_finish[0], "")
                    is_multiline_comment = False
                else:
                    lines[i] = ""

        return lines
