from enum import Enum


class LineTypes(Enum):
    FROM = "from"
    IMPORT = "import"
    CLASS = "class"
    DEF = "def"
    RETURN = "return"
    FOR = "for"
    WHILE = "while"
    IF = "if"
    ELIF = "elif"
    ELSE = "else"
    TRY = "try"
    EXCEPT = "except"
    # These types are not useable as comparators
    ASSIGNMENT = "__assignment__"
    OPERATION = "__operation__"
    EMPTY = "__empty__"
    DECORATOR = "__decorator__"
