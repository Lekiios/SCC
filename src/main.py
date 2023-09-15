from cLexer import Lexer
from cParser import Parser
from generator import Generator
from sem_ana import SemAna
from symbol_table import SymbolTable
import time

start = time.time()

# Init parser content
lexer = Lexer("../tests/test.c")
lexer.next()
parser = Parser(lexer)
sem_analyzer = SemAna()
generator = Generator()


while lexer.token["type"] != "EOF":
    p = parser.parse()
    sem_analyzer.analyse(p)
    generator.gencode(p)

print('.start')
print('prep main')
print('call 0')
print('halt')

end = time.time()
print("\nTime elapsed: " + str(round((end - start)*1000, 3)) + 'ms')
