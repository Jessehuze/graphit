import tokenize


class AugTokGen:
    def __init__(self, file: str = None):
        if file is None:
            self.tokgen = None
        else:
            try:
                readline = open(file).readline
                self.tokgen = tokenize.generate_tokens(readline)
            except FileNotFoundError:
                raise FileNotFoundError("FileName: " + file + "was not found.")

    def __iter__(self):
        return self

    def __next__(self):
        next(self.tokgen)

    def load_file(self, file):
        try:
            readline = open(file).readline
            self.tokgen = tokenize.generate_tokens(readline)
        except FileNotFoundError:
            raise FileNotFoundError("FileName: " + file + "was not found.")

    def load_readline(self, readline):
        self.tokgen = tokenize.generate_tokens(readline)

    def readline(self):
        try:
            token_list = [next(self.tokgen)]
        except StopIteration:
            raise StopIteration

        while not self.is_newline(token_list[-1]):
            token_list.append(next(self.tokgen))
        return token_list

    def is_newline(self, token):
        return self.get_token_type(token) == "NL" or self.get_token_type(token) == "NEWLINE"

    @staticmethod
    def get_token_type(token):
        return tokenize.tok_name.get(token.type, token)
