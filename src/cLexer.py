class Lexer:
    keywords = ["int", "for", "while", "if", "else", "break", "continue", "return"]

    def __init__(self, path):
        self.token = dict()
        self.last = dict()
        self.content = ""

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

        # (
        elif self.content[0] == '(':
            self.token = {"type": "("}
            self.content = self.content[1:]

        # )
        elif self.content[0] == ')':
            self.token = {"type": ")"}
            self.content = self.content[1:]

        # ! and !=
        elif self.content[0] == "!":
            if len(self.content) >= 2 and self.content[1] == "=":
                self.token = {"type": "!="}
                self.content = self.content[2:]
            else:
                self.token = {"type": "!"}
                self.content = self.content[1:]

        # ;
        elif self.content[0] == ";":
            self.token = {"type": ";"}
            self.content = self.content[1:]

        return True
