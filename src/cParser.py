class Parser:
    def __init__(self, path):
        self.token = dict()
        self.last = dict()
        self.content = ""
        self.pos = 0

        file = open(path, "r")
        content_tab = file.readlines()
        file.close()

        for string in content_tab:
            self.content = self.content + string

        self.content = self.content.replace("\n", "")

    def next(self):
        last = self.token

        while self.content[self.pos].isspace():
            self.pos = self.pos + 1

    def check(self, t):
        if self.token["type"] == t:
            self.next()
            return True
        return False

    def accept(self, t):
        if not self.check(t):
            raise Exception("Parser error !")
