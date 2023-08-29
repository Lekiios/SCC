
global token
global last

file = open("../tests/parser_test-1.c", "r")
content_tab = file.readlines()
file.close()

content = ""
for string in content_tab:
    content = content + string

content = content.replace("\n", "")

for char in content:
    int(char)

#def next():
#    last = token
#    token = read()


