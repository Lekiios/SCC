from src.symbol_table import SymbolTable

symbol_table = SymbolTable()

symbol_table.declare("test")
print(symbol_table.find("test"))
print(symbol_table.vars)
symbol_table.begin()
print(symbol_table.find("test"))
symbol_table.declare("test")
print(symbol_table.find("test"))
print(symbol_table.vars)
symbol_table.end()
print(symbol_table.vars)