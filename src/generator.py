def gencode(node):
    match node.type:
        case "nd_const":
            print('PUSH {}'.format(node.value))
        case "nd_not":
            gencode(node.children[0])
            print("NOT")
        case "nd_u_add":
            gencode(node.children[0])
            print("ADD")
        case "nd_u_sub":
            gencode(node.children[0])
            print("SUB")

