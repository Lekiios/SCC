from cLexer import Lexer
from cParser import Parser, Node
from generator import gencode
import time

start = time.time()

# Init parser content
lexer = Lexer("../tests/test.c")
lexer.next()
parser = Parser(lexer)

while lexer.token["type"] != "EOF":
    p = parser.parse()
    # TODO Semantic analysis
    gencode(p)

end = time.time()
print("\nTime elapsed: " + str(round((end - start)*1000, 3)) + 'ms')
