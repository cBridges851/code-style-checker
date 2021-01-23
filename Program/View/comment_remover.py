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
        
        # Initial value for the variable that switches to True if a multiline 
        # comment has started 
        is_multiline_comment = False

        # Loops through each line
        for i in range(len(lines)):
            # Looks for single line comments indicated by //
            single_line_comment = re.findall(r"//.+", lines[i])
            # Looks for the start of a multiline comment indicated by /*, 
            # with some text potentially after it
            multiline_comment_start = re.findall(r"/\*(.+)?", lines[i])
            # Looks for the end of a multiline comment indicated by */,
            # with some text potentially before it
            multiline_comment_finish = re.findall(r"(.+)?\*/", lines[i])

            # If there are single line comments on the line
            if len(single_line_comment) != 0:
                # Replace the comment with an empty string to remove it
                lines[i] = lines[i].replace(single_line_comment[0], "")
            
            # Check if the line is currently part of a multiline comment
            if not is_multiline_comment:
                # Check if multiline started
                if len(multiline_comment_start) != 0:
                    # Replace /* and any text after it on the line with an 
                    # empty string to remove it
                    lines[i] = lines[i].replace(multiline_comment_start[0], "")
                    # Indicate that the multiline comment has started
                    is_multiline_comment = True

                # In case the multiline comment finishes on the line
                if len(multiline_comment_finish) != 0:
                    # Remove */ and any text before it
                    lines[i] = lines[i].replace(multiline_comment_finish[0], "")
                    # Indicate the multiline comment has finished
                    is_multiline_comment = False
            # If the line is part of a multiline comment
            else:
                # If */ is apparent in the line
                if len(multiline_comment_finish) != 0:
                    # Remove */ and any text before it
                    lines[i] = lines[i].replace(multiline_comment_finish[0], "")
                    # Indicate the multiline comment has finished
                    is_multiline_comment = False
                else:
                    # Remove all text in the line, multiline comment is still apparent
                    lines[i] = ""

        # Returns the lines with the comments removed
        return lines
