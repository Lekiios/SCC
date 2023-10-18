from cLexer import Lexer
from cParser import Parser
from generator import Generator
from sem_ana import SemAna
import time


def compile_files(*path):
    lexer = Lexer(path)
    parser = Parser(lexer)
    sem_analyzer = SemAna()
    generator = Generator()

    while lexer.token["type"] != "EOF":
        p = parser.parse()
        sem_analyzer.analyse(p)
        generator.gencode(p)


start = time.time()

compile_files('../std/lib.c', '../tests/test.c')

print('.start')
print('prep init')
print('call 0')
print('prep main')
print('call 0')
print('halt')

end = time.time()
print("\nTime elapsed: " + str(round((end - start) * 1000, 3)) + 'ms')
