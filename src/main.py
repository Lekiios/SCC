from cParser import Parser
import time

start = time.time()

# Init parser content
parser = Parser("../tests/parser_test-1.c")

while parser.next():
    print(parser.token)
print(parser.token)

end = time.time()
print("\nTime elapsed: " + str(end - start) + ' s')
