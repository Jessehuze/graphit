from enum import Enum


class LineType(Enum):
    FROM = "from"
    IMPORT = "import"
    CLASS = "class"
    FUNC_DEF = "def"
    RETURN = "return"
    FOR = "for"
    WHILE = "while"
    IF = "if"
    ELIF = "elif"
    ELSE = "else"
    TRY = "try"
    EXCEPT = "except"
    # These types aren't suitable as comparators
    OPERATIONAL = "__operational__"
    BLANK = "__blank__"
    DECORATOR = "__decorator__"

    @staticmethod
    def get_value(word):
        if word is None or word.isspace() or word == '':
            return LineType.BLANK
        try:
            word = word.strip(':')
            return LineType(word)
        except ValueError:
            if len(word):
                if word[0] == '@':
                    return LineType.DECORATOR
            return LineType.OPERATIONAL
