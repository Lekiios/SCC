from cLexer import Lexer
from cParser import Parser
from generator import Generator
from sem_ana import SemAna
import time


def compile_files(*path):
    lexer = Lexer(path)
    parser = Parser(lexer)
    sem_analyzer = SemAna()
    generator = Generator('../tests/sim')

    while lexer.token["type"] != "EOF":
        p = parser.parse()
        sem_analyzer.analyse(p)
        generator.gencode(p)

    generator.write_bin('.start')
    generator.write_bin('prep init')
    generator.write_bin('call 0')
    generator.write_bin('prep main')
    generator.write_bin('call 0')
    generator.write_bin('halt')

    generator.write_file()


start = time.time()

compile_files('../std/lib.c', '../tests/sim/main.c')

end = time.time()
print("\nTime elapsed: " + str(round((end - start) * 1000, 3)) + 'ms')
