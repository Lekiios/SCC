from cLexer import Lexer
import time

start = time.time()

# Init parser content
lexer = Lexer("../tests/parser_test-1.c")

while lexer.next():
    print(lexer.token)
print(lexer.token)

end = time.time()
print("\nTime elapsed: " + str(end - start) + 's')
