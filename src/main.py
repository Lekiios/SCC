from cLexer import Lexer
from cParser import Parser
from generator import gencode
from sem_ana import SemAna
from symbol_table import SymbolTable
import time

start = time.time()

# Init parser content
lexer = Lexer("../tests/test.c")
lexer.next()
parser = Parser(lexer)
sem_analyzer = SemAna()

while lexer.token["type"] != "EOF":
    p = parser.parse()
    sem_analyzer.analyse(p)
    print('resn {}'.format(sem_analyzer.nb_var))
    gencode(p)
    print('drop {}'.format(sem_analyzer.nb_var))

print('halt')

end = time.time()
print("\nTime elapsed: " + str(round((end - start)*1000, 3)) + 'ms')
