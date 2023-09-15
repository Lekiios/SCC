from symbol_table import SymbolTable


class SemAna:

    def __init__(self):
        self.symbol_table = SymbolTable()
        self.nb_var = 0

    def analyse(self, node):
        match node.type:
            case 'nd_block':
                self.symbol_table.begin()
                for child in node.children:
                    self.analyse(child)
                self.symbol_table.end()
            case 'nd_decl':
                s = self.symbol_table.declare(node.value)
                s['address'] = self.nb_var
                self.nb_var += 1
                s['type'] = 'var_loc'
            case 'nd_ref':
                s = self.symbol_table.find(node.value)
                node.symbol = s
            case 'nd_func':
                self.nb_var = 0
                s = self.symbol_table.declare(node.value)
                self.symbol_table.begin()
                for child in node.children:
                    self.analyse(child)
                self.symbol_table.end()
                s['type'] = 'symb_func'
                s['nb_var'] = self.nb_var - (len(node.children) - 1)
                node.symbol = s
            case other:
                for child in node.children:
                    self.analyse(child)
