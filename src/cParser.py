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
        elif self.lexer.check('*'):
            n = self.prefix()
            return Node('nd_ind', children=[n])
        elif self.lexer.check('&'):
            n = self.prefix()
            return Node('nd_adr', children=[n])
        else:
            n = self.suffix()
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
        elif self.lexer.check('return'):
            n = self.expression(0)
            self.lexer.accept(';')
            return Node('nd_ret', children=[n])
        elif self.lexer.check('int'):
            n = Node('nd_seq')
            while True:
                self.lexer.accept('id')
                n.children.append(Node('nd_decl', value=self.lexer.last['value']))
                if not self.lexer.check(','):
                    break
            self.lexer.accept(';')
            return n
        elif self.lexer.check('if'):
            self.lexer.accept('(')
            cond = self.expression(0)
            self.lexer.accept(')')
            i1 = self.instructions()
            i2 = None
            if self.lexer.check('else'):
                i2 = self.instructions()
            n = Node('nd_cond', children=[cond, i1])
            if i2 is not None:
                n.children.append(i2)
            return n
        elif self.lexer.check('while'):
            self.lexer.accept('(')
            cond = self.expression(0)
            self.lexer.accept(')')
            i = self.instructions()
            loop = Node('nd_loop')
            target = Node('nd_target')
            nd_cond = Node('nd_cond')
            nd_break = Node('nd_break')
            loop.children.append(target)
            loop.children.append(nd_cond)
            nd_cond.children.append(cond)
            nd_cond.children.append(i)
            nd_cond.children.append(nd_break)
            return loop
        elif self.lexer.check('break'):
            self.lexer.accept(';')
            return Node('nd_break')
        elif self.lexer.check('continue'):
            self.lexer.accept(';')
            return Node('nd_continue')
        else:
            n = self.expression(0)
            self.lexer.accept(';')
            return Node('nd_drop', children=[n])

    def suffix(self):
        n = self.atom()
        if self.lexer.check('('):
            n = Node('nd_call', children=[n])
            while not self.lexer.check(')'):
                n.children.append(self.expression(0))
                if self.lexer.check(')'):
                    break
                self.lexer.accept(',')
        return n

    def function(self):
        self.lexer.accept('int')
        self.lexer.accept('id')
        n = Node('nd_func', value=self.lexer.last['value'])
        self.lexer.accept('(')
        while self.lexer.check('int'):
            self.lexer.accept('id')
            n.children.append(Node('nd_decl', value=self.lexer.last['value']))
            if self.lexer.check(','):
                continue
            break
        self.lexer.accept(')')
        n.children.append(self.instructions())
        return n

    def parse(self):
        return self.function()


class Node:
    def __init__(self, _type, children=None, value=None):
        self.type = _type
        if children:
            self.children = children
        else:
            self.children = []
        self.value = value
        self.symbol = dict()
