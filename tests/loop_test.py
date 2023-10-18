import sys

from src.scc import compile_files

def compile_in_var(path):
    var = ''
    with var as sys.stdout:
        compile_files(path)
    return var

def simple_while_test():
    asm = compile_in_var('./toto')
    print(asm)

simple_while_test()