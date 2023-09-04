class SymbolTable:

    def __init__(self):
        self.vars = [dict()]

    def declare(self, name):
        if name in self.vars[-1]:
            raise Exception('Cannot declare {}, already declared in scope'.format(name))
        var = {'type': '', 'address': ''}
        self.vars[-1][name] = var
        return var

    def find(self, name):
        for table in self.vars[::-1]:
            if name in table:
                return table[name]
        raise Exception('{} is not declared in scope'.format(name))

    def begin(self):
        self.vars.append(dict())

    def end(self):
        self.vars.pop()
