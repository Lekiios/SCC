class Parser:
    operators = {
        '=': {'nd': 'nd_affect', 'prio': 1, 'ra': 1},
        '||': {'nd': 'nd_or', 'prio': 2, 'ra': 0},
        '&&': {'nd': 'nd_and', 'prio': 3, 'ra': 0},
        '==': {'nd': 'nd_eq', 'prio': 4, 'ra': 0},
        '!=': {'nd': 'nd_not_eq', 'prio': 4, 'ra': 0},
        '<': {'nd': 'nd_inf', 'prio': 5, 'ra': 0},
        '>': {'nd': 'nd_sup', 'prio': 5, 'ra': 0},
        '<=': {'nd': 'nd_inf_eq', 'prio': 5, 'ra': 0},
        '>=': {'nd': 'nd_sup_eq', 'prio': 5, 'ra': 0},
        '+': {'nd': 'nd_add', 'prio': 6, 'ra': 0},
        '-': {'nd': 'nd_sub', 'prio': 6, 'ra': 0},
        '*': {'nd': 'nd_mult', 'prio': 7, 'ra': 0},
        '/': {'nd': 'nd_div', 'prio': 7, 'ra': 0},
        '%': {'nd': 'nd_mod', 'prio': 7, 'ra': 0},
    }

    def __init__(self, lexer):
        self.lexer = lexer

    def atom(self):
        if self.lexer.check("const"):
            return Node("nd_const", value=self.lexer.last["value"])
        elif self.lexer.check("id"):
            return Node('nd_ref', value=self.lexer.last['value'])
        elif self.lexer.check("("):
            n = self.expression(0)
            self.lexer.accept(")")
            return n
        else:
            raise Exception("Parser Error !")

    def prefix(self):
        if self.lexer.check("-"):
            n = self.prefix()
            return Node("nd_u_sub", children=[n])
        elif self.lexer.check("!"):
            n = self.prefix()
            return Node("nd_not", children=[n])
        elif self.lexer.check("+"):
            n = self.prefix()
            return Node("nd_u_add", children=[n])
        else:
            n = self.atom()
            return n

    def expression(self, prio_min):
        n = self.prefix()
        try:
            while self.operators[self.lexer.token['type']] is not None:
                op = self.operators[self.lexer.token['type']]
                if op['prio'] <= prio_min:
                    break
                self.lexer.next()
                m = self.expression(op['prio'] - op['ra'])
                n = Node(op['nd'], children=[n, m])
        except KeyError:
            return n
        return n

    def instructions(self):
        if self.lexer.check(';'):
            return Node('nd_empty')
        elif self.lexer.check('{'):
            n = Node('nd_block')
            while not self.lexer.check('}'):
                n.children.append(self.instructions())
            return n
        elif self.lexer.check('debug'):
            n = self.expression(0)
            self.lexer.accept(';')
            return Node('nd_debug', children=[n])
        elif self.lexer.check('int'):
            n = Node('nd_seq')
            while True:
                self.lexer.accept('id')
                n.children.append(Node('nd_decl', value=self.lexer.last['value']))
                if not self.lexer.check(','):
                    break
            self.lexer.accept(';')
            return n
        else:
            n = self.expression(0)
            self.lexer.accept(';')
            return Node('nd_drop', children=[n])

    def parse(self):
        return self.instructions()


class Node:
    def __init__(self, _type, children=None, value=None):
        self.type = _type
        if children:
            self.children = children
        else:
            self.children = []
        self.value = value
        self.symbol = dict()
