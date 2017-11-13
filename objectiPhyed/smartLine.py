import tokenize


class SmartLine:
    def __init__(self, token_list, parent=None):
        self.token_list = token_list
        self.parent = parent
        self.num_indents = 0
        self.line_type = None
        self.raw_text = None
        self.nl_rm_text = None

        # Set Raw Text and text with NL removed for printing
        if len(self.token_list):
            line = self.token_list[0].line
            self.raw_text = line
            if line[-1] == '\n':
                self.nl_rm_text = line[:-1]
            else:
                self.nl_rm_text = line

        # Set number of indents
        if self.raw_text:
            if self.raw_text[0] == ' ':
                for i, char in enumerate(self.raw_text):
                    # End of spaces, not mixing tabs and spaces, num spaces
                    # is divisible by 4
                    if char != ' ' and char != '\t' and (i % 4 == 0):
                        self.num_indents = int(i / 4)
                        break
                    elif char == '\t':
                        raise RuntimeError('Data is Malformed: ' + self.nl_rm_text)
            elif self.raw_text[0] == '\t':
                for i, char in enumerate(self.raw_text):
                    # End of tabs and not mixing spaces in
                    if char != '\t' and char != ' ':
                        self.num_indents = i
                        break
                    elif char == ' ':
                        raise RuntimeError('Data is Malformed: ' + self.nl_rm_text)

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return self.nl_rm_text

    def set_parent(self, parent):
        self.parent = parent

    def get_raw(self):
        return str(self.token_list)
