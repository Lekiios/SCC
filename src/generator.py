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
        case 'nd_sub':
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
        case 'nd_and':
            gencode(node.children[0])
            gencode(node.children[1])
            print('and')
        case 'nd_eq':
            gencode(node.children[0])
            gencode(node.children[1])
            print('cmpeq')
        case 'nd_not_eq':
            gencode(node.children[0])
            gencode(node.children[1])
            print('cmpne')
        case 'nd_inf':
            gencode(node.children[0])
            gencode(node.children[1])
            print('cmplt')
        case 'nd_inf_eq':
            gencode(node.children[0])
            gencode(node.children[1])
            print('cmple')
        case 'nd_sup':
            gencode(node.children[0])
            gencode(node.children[1])
            print('cmpgt')
        case 'nd_sup_eq':
            gencode(node.children[0])
            gencode(node.children[1])
            print('cmpge')

        # TODO : affectation

        case 'nd_drop':
            gencode(node.children[0])
            print('drop 1')

        case 'nd_debug':
            gencode(node.children[0])
            print('dbg')

        case other:
            raise Exception('Generation failed!')
