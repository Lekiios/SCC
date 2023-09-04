class Lexer:
    keywords = ["int", "for", "while", "if", "else", "break", "continue", "return", "debug"]

    def __init__(self, path=None):
        self.token = dict()
        self.last = dict()
        self.content = ""

        if path:
            file = open(path, "r")
            content_tab = file.readlines()
            file.close()

            for string in content_tab:
                self.content = self.content + string

            self.content = self.content.replace("\n", "")

    def check(self, t):
        if self.token["type"] == t:
            self.next()
            return True
        return False

    def accept(self, t):
        if not self.check(t):
            if t == ')':
                raise Exception('Missing closing parenthesis !')
            else:
                raise Exception("Lexer error !")

    def iskeyword(self, k):
        return k in self.keywords

    def next(self):
        self.last = self.token

        # EOF
        if len(self.content) < 1:
            self.token = {"type": "EOF"}
            return False

        while self.content[0].isspace():
            self.content = self.content[1:]

        # CONST
        if self.content[0].isdigit():
            self.token = {"type": "const", "value": ""}
            while len(self.content) >= 1 and self.content[0].isdigit():
                self.token["value"] = self.token["value"] + self.content[0]
                self.content = self.content[1:]
        # IDs
        elif self.content[0].isalpha():
            self.token = {"type": "id", "value": ""}
            while len(self.content) >= 1 and (self.content[0].isalpha() or self.content[0].isdigit()):
                self.token["value"] = self.token["value"] + self.content[0]
                self.content = self.content[1:]
            if self.iskeyword(self.token["value"]):
                self.token = {"type": self.token["value"]}

        # +
        elif self.content[0] == '+':
            self.token = {"type": "+"}
            self.content = self.content[1:]

        # -
        elif self.content[0] == '-':
            self.token = {"type": "-"}
            self.content = self.content[1:]

        # *
        elif self.content[0] == '*':
            self.token = {"type": "*"}
            self.content = self.content[1:]

        # /
        elif self.content[0] == '/':
            self.token = {"type": "/"}
            self.content = self.content[1:]

        # %
        elif self.content[0] == '%':
            self.token = {"type": "%"}
            self.content = self.content[1:]

        # = and ==
        elif self.content[0] == '=':
            if len(self.content) >= 2 and self.content[1] == '=':
                self.token = {"type": "=="}
                self.content = self.content[2:]
            else:
                self.token = {"type": "="}
                self.content = self.content[1:]

        # ! and !=
        elif self.content[0] == "!":
            if len(self.content) >= 2 and self.content[1] == "=":
                self.token = {"type": "!="}
                self.content = self.content[2:]
            else:
                self.token = {"type": "!"}
                self.content = self.content[1:]

        # < and <=
        elif self.content[0] == "<":
            if len(self.content) >= 2 and self.content[1] == '=':
                self.token = {'type': '<='}
                self.content = self.content[2:]
            else:
                self.token = {'type': '<'}
                self.content = self.content[1:]

        # > and >=
        elif self.content[0] == ">":
            if len(self.content) >= 2 and self.content[1] == '=':
                self.token = {'type': '>='}
                self.content = self.content[2:]
            else:
                self.token = {'type': '>'}
                self.content = self.content[1:]

        # ||
        elif len(self.content) >= 2 and self.content[0:2] == '||':
            self.token = {'type': '||'}
            self.content = self.content[2:]

        # & and &&
        elif self.content[0] == '&':
            if len(self.content) >= 2 and self.content[1] == '&':
                self.token = {'type': '&&'}
                self.content = self.content[2:]
            else:
                self.token = {'type': '&'}
                self.content = self.content[1:]

        # (
        elif self.content[0] == '(':
            self.token = {"type": "("}
            self.content = self.content[1:]

        # )
        elif self.content[0] == ')':
            self.token = {"type": ")"}
            self.content = self.content[1:]

        # [
        elif self.content[0] == '[':
            self.token = {"type": "["}
            self.content = self.content[1:]

        # ]
        elif self.content[0] == ']':
            self.token = {"type": "]"}
            self.content = self.content[1:]

        # {
        elif self.content[0] == '{':
            self.token = {"type": "{"}
            self.content = self.content[1:]

        # }
        elif self.content[0] == '}':
            self.token = {"type": "}"}
            self.content = self.content[1:]

        # ,
        elif self.content[0] == ",":
            self.token = {"type": ","}
            self.content = self.content[1:]

        # ;
        elif self.content[0] == ";":
            self.token = {"type": ";"}
            self.content = self.content[1:]

        else:
            raise Exception('Lexer Error: token not defined !')
        return True
