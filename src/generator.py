def gencode(node):
    match node.type:
        case "nd_const":
            print('push {}'.format(node.value))
        case "nd_not":
            gencode(node.children[0])
            print("not")
        case "nd_u_add":
            gencode(node.children[0])
            print("add")
        case "nd_u_sub":
            gencode(node.children[0])
            print("sub")

        # BINARY OPERATORS
        case 'nd_add':
            gencode(node.children[0])
            gencode(node.children[1])
            print('add')
        case'nd_sub':
            gencode(node.children[0])
            gencode(node.children[1])
            print('sub')
        case 'nd_mult':
            gencode(node.children[0])
            gencode(node.children[1])
            print('mul')
        case 'nd_div':
            gencode(node.children[0])
            gencode(node.children[1])
            print('div')
        case 'nd_mod':
            gencode(node.children[0])
            gencode(node.children[1])
            print('mod')
        case 'nd_or':
            gencode(node.children[0])
            gencode(node.children[1])
            print('or')