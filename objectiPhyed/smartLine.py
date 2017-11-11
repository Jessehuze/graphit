import tokenize


class SmartLine:
    def __init__(self, token_list, parent=None):
        self.token_list = token_list
        self.parent = parent
        self.num_idents = None
        self.line_type = None
        self.line_text = None
        if len(self.token_list):
            line = self.token_list[0].line
            if line[-1] == '\n':
                self.line_text = line[:-1]
            else:
                self.line_text = line

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return self.line_text

    def set_parent(self, parent):
        self.parent = parent

    def get_raw(self):
        return str(self.token_list)
