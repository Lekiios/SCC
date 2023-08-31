class Parser:

    def __init__(self, lexer):
        self.lexer = lexer

    def atom(self):
        if self.lexer.check("const"):
            return Node("nd_const", None, self.lexer.last["value"])
        elif self.lexer.check("id"):
            # TODO
            raise Exception("Parser error !")
        elif self.lexer.check("("):
            n = self.expression()
            self.lexer.accept(")")
            return n
        else:
            raise Exception("Parser Error !")

    def prefix(self):
        if self.lexer.check("-"):
            n = self.prefix()
            return Node("nd_u_sub", [n])
        elif self.lexer.check("!"):
            n = self.prefix()
            return Node("nd_not", [n])
        elif self.lexer.check("+"):
            n = self.prefix()
            return Node("nd_u_add", [n])
        else:
            n = self.atom()
            return n

    def expression(self):
        return self.prefix()

    def parse(self):
        return self.expression()


class Node:
    def __init__(self, _type, children=None, value=None):
        self.type = _type
        self.children = children
        self.value = value
