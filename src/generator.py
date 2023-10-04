class Generator:

    def __init__(self):
        self.nb_label = 0
        self.lbl_continue = 0
        self.lbl_break = 0

    def gencode(self, node):
        match node.type:
            case "nd_const":
                print('push {}'.format(node.value))
            case "nd_not":
                self.gencode(node.children[0])
                print("not")
            case "nd_u_add":
                self.gencode(node.children[0])
                print("add")
            case "nd_u_sub":
                print('push 0')
                self.gencode(node.children[0])
                print("sub")

            # BINARY OPERATORS
            case 'nd_add':
                self.gencode(node.children[0])
                self.gencode(node.children[1])
                print('add')
            case 'nd_sub':
                self.gencode(node.children[0])
                self.gencode(node.children[1])
                print('sub')
            case 'nd_mult':
                self.gencode(node.children[0])
                self.gencode(node.children[1])
                print('mul')
            case 'nd_div':
                self.gencode(node.children[0])
                self.gencode(node.children[1])
                print('div')
            case 'nd_mod':
                self.gencode(node.children[0])
                self.gencode(node.children[1])
                print('mod')
            case 'nd_or':
                self.gencode(node.children[0])
                self.gencode(node.children[1])
                print('or')
            case 'nd_and':
                self.gencode(node.children[0])
                self.gencode(node.children[1])
                print('and')
            case 'nd_eq':
                self.gencode(node.children[0])
                self.gencode(node.children[1])
                print('cmpeq')
            case 'nd_not_eq':
                self.gencode(node.children[0])
                self.gencode(node.children[1])
                print('cmpne')
            case 'nd_inf':
                self.gencode(node.children[0])
                self.gencode(node.children[1])
                print('cmplt')
            case 'nd_inf_eq':
                self.gencode(node.children[0])
                self.gencode(node.children[1])
                print('cmple')
            case 'nd_sup':
                self.gencode(node.children[0])
                self.gencode(node.children[1])
                print('cmpgt')
            case 'nd_sup_eq':
                self.gencode(node.children[0])
                self.gencode(node.children[1])
                print('cmpge')

            case 'nd_affect':
                self.gencode(node.children[1])
                print('dup')
                if node.children[0].type == 'nd_ref' and node.children[0].symbol['type'] == 'var_loc':
                    print('set {}'.format(node.children[0].symbol['address']))
                elif node.children[0].type == 'nd_ind':
                    self.gencode(node.children[0].children[0])
                    print('write')
                else:
                    raise Exception('Affectation Error !')

            case 'nd_ref':
                if node.symbol['type'] == 'var_loc':
                    print('get {}'.format(node.symbol['address']))
                else:
                    raise Exception('Do not handle other symbol than var_loc !')
            case 'nd_decl':
                pass

            case 'nd_block' | 'nd_seq':
                for child in node.children:
                    self.gencode(child)
            case 'nd_drop':
                self.gencode(node.children[0])
                print('drop 1')

            case 'nd_cond':
                if len(node.children) == 2:
                    l1 = self.nb_label
                    self.nb_label += 1
                    self.gencode(node.children[0])
                    print('jumpf l{} ; if'.format(l1))
                    self.gencode(node.children[1])
                    print('.l{} ; end if'.format(l1))
                else:
                    l1 = self.nb_label
                    self.nb_label += 1
                    l2 = self.nb_label
                    self.nb_label += 1
                    self.gencode(node.children[0])
                    print('jumpf l{} ; if'.format(l1))
                    self.gencode(node.children[1])
                    print('jump l{}'.format(l2))
                    print('.l{} ; else'.format(l1))
                    self.gencode(node.children[2])
                    print('.l{}'.format(l2))

            case 'nd_target':
                print('.l{}'.format(self.lbl_continue))
            case 'nd_break':
                print('jump l{}'.format(self.lbl_break))
            case 'nd_continue':
                print('jump l{}'.format(self.lbl_continue))
            case 'nd_loop':
                lbl_begin = self.nb_label
                self.nb_label += 1
                save_break = self.lbl_break
                save_continue = self.lbl_continue
                self.lbl_break = self.nb_label
                self.nb_label += 1
                self.lbl_continue = self.nb_label
                self.nb_label += 1
                print('.l{}'.format(lbl_begin))
                for child in node.children:
                    self.gencode(child)
                print('jump l{}'.format(lbl_begin))
                print('.l{}'.format(self.lbl_break))
                self.lbl_continue = save_continue
                self.lbl_break = save_break
            case 'nd_func':
                print('.{}'.format(node.value))
                print('resn {}'.format(node.symbol['nb_var']))
                self.gencode(node.children[-1])
                print('push 0')
                print('ret')
            case 'nd_call':
                if node.children[0].type != 'nd_ref':
                    raise Exception('generator Error while calling function')
                if node.children[0].symbol['type'] != 'symb_func':
                    raise Exception('Cannot call anything else than a function !')
                print('prep {}'.format(node.children[0].value))
                for child in node.children[1:]:
                    self.gencode(child)
                print('call {}'.format(len(node.children) - 1))
            case 'nd_ret':
                self.gencode(node.children[0])
                print('ret')

            case 'nd_ind':
                self.gencode(node.children[0])
                print('read')
            case 'nd_adr':
                if node.children[0].type != 'nd_ref':
                    raise Exception('Need an identifier to access memory address !')
                else:
                    print('prep start')
                    print('swap')
                    print('drop 1')
                    print('push {}'.format(node.children[0].symbol['address']+1))
                    print('sub')

            case 'nd_debug':
                self.gencode(node.children[0])
                print('dbg')

            case 'nd_send':
                self.gencode(node.children[0])
                print('send')

            case other:
                raise Exception('Generation failed!')
