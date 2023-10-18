class Generator:

    def __init__(self):
        self.nb_label = 0
        self.lbl_continue = 0
        self.lbl_break = 0
        self.asm = ''
        
    def write_bin(self, instr):
        self.asm += instr + '\n'

    def write_file(self):
        file = open("./asm.s", "w")
        file.write(self.asm)
        file.close()

    def gencode(self, node):
        match node.type:
            case "nd_const":
                self.write_bin('push {}'.format(node.value))
            case "nd_not":
                self.gencode(node.children[0])
                self.write_bin("not")
            case "nd_u_add":
                self.gencode(node.children[0])
                self.write_bin("add")
            case "nd_u_sub":
                self.write_bin('push 0')
                self.gencode(node.children[0])
                self.write_bin("sub")

            # BINARY OPERATORS
            case 'nd_add':
                self.gencode(node.children[0])
                self.gencode(node.children[1])
                self.write_bin('add')
            case 'nd_sub':
                self.gencode(node.children[0])
                self.gencode(node.children[1])
                self.write_bin('sub')
            case 'nd_mult':
                self.gencode(node.children[0])
                self.gencode(node.children[1])
                self.write_bin('mul')
            case 'nd_div':
                self.gencode(node.children[0])
                self.gencode(node.children[1])
                self.write_bin('div')
            case 'nd_mod':
                self.gencode(node.children[0])
                self.gencode(node.children[1])
                self.write_bin('mod')
            case 'nd_or':
                self.gencode(node.children[0])
                self.gencode(node.children[1])
                self.write_bin('or')
            case 'nd_and':
                self.gencode(node.children[0])
                self.gencode(node.children[1])
                self.write_bin('and')
            case 'nd_eq':
                self.gencode(node.children[0])
                self.gencode(node.children[1])
                self.write_bin('cmpeq')
            case 'nd_not_eq':
                self.gencode(node.children[0])
                self.gencode(node.children[1])
                self.write_bin('cmpne')
            case 'nd_inf':
                self.gencode(node.children[0])
                self.gencode(node.children[1])
                self.write_bin('cmplt')
            case 'nd_inf_eq':
                self.gencode(node.children[0])
                self.gencode(node.children[1])
                self.write_bin('cmple')
            case 'nd_sup':
                self.gencode(node.children[0])
                self.gencode(node.children[1])
                self.write_bin('cmpgt')
            case 'nd_sup_eq':
                self.gencode(node.children[0])
                self.gencode(node.children[1])
                self.write_bin('cmpge')

            case 'nd_affect':
                self.gencode(node.children[1])
                self.write_bin('dup')
                if node.children[0].type == 'nd_ref' and node.children[0].symbol['type'] == 'var_loc':
                    self.write_bin('set {}'.format(node.children[0].symbol['address']))
                elif node.children[0].type == 'nd_ind':
                    self.gencode(node.children[0].children[0])
                    self.write_bin('write')
                else:
                    raise Exception('Affectation Error !')

            case 'nd_ref':
                if node.symbol['type'] == 'var_loc':
                    self.write_bin('get {}'.format(node.symbol['address']))
                else:
                    raise Exception('Do not handle other symbol than var_loc !')
            case 'nd_decl':
                pass

            case 'nd_block' | 'nd_seq':
                for child in node.children:
                    self.gencode(child)
            case 'nd_drop':
                self.gencode(node.children[0])
                self.write_bin('drop 1')

            case 'nd_cond':
                if len(node.children) == 2:
                    l1 = self.nb_label
                    self.nb_label += 1
                    self.gencode(node.children[0])
                    self.write_bin('jumpf l{} ; if'.format(l1))
                    self.gencode(node.children[1])
                    self.write_bin('.l{} ; end if'.format(l1))
                else:
                    l1 = self.nb_label
                    self.nb_label += 1
                    l2 = self.nb_label
                    self.nb_label += 1
                    self.gencode(node.children[0])
                    self.write_bin('jumpf l{} ; if'.format(l1))
                    self.gencode(node.children[1])
                    self.write_bin('jump l{}'.format(l2))
                    self.write_bin('.l{} ; else'.format(l1))
                    self.gencode(node.children[2])
                    self.write_bin('.l{}'.format(l2))

            case 'nd_target':
                self.write_bin('.l{}'.format(self.lbl_continue))
            case 'nd_break':
                self.write_bin('jump l{}'.format(self.lbl_break))
            case 'nd_continue':
                self.write_bin('jump l{}'.format(self.lbl_continue))
            case 'nd_loop':
                lbl_begin = self.nb_label
                self.nb_label += 1
                save_break = self.lbl_break
                save_continue = self.lbl_continue
                self.lbl_break = self.nb_label
                self.nb_label += 1
                self.lbl_continue = self.nb_label
                self.nb_label += 1
                self.write_bin('.l{}'.format(lbl_begin))
                for child in node.children:
                    self.gencode(child)
                self.write_bin('jump l{}'.format(lbl_begin))
                self.write_bin('.l{}'.format(self.lbl_break))
                self.lbl_continue = save_continue
                self.lbl_break = save_break
            case 'nd_func':
                self.write_bin('.{}'.format(node.value))
                self.write_bin('resn {}'.format(node.symbol['nb_var']))
                self.gencode(node.children[-1])
                self.write_bin('push 0')
                self.write_bin('ret')
            case 'nd_call':
                if node.children[0].type != 'nd_ref':
                    raise Exception('generator Error while calling function')
                if node.children[0].symbol['type'] != 'symb_func':
                    raise Exception('Cannot call anything else than a function !')
                self.write_bin('prep {}'.format(node.children[0].value))
                for child in node.children[1:]:
                    self.gencode(child)
                self.write_bin('call {}'.format(len(node.children) - 1))
            case 'nd_ret':
                self.gencode(node.children[0])
                self.write_bin('ret')

            case 'nd_ind':
                self.gencode(node.children[0])
                self.write_bin('read')
            case 'nd_adr':
                if node.children[0].type != 'nd_ref':
                    raise Exception('Need an identifier to access memory address !')
                else:
                    self.write_bin('prep start')
                    self.write_bin('swap')
                    self.write_bin('drop 1')
                    self.write_bin('push {}'.format(node.children[0].symbol['address']+1))
                    self.write_bin('sub')

            case 'nd_debug':
                self.gencode(node.children[0])
                self.write_bin('dbg')

            case 'nd_send':
                self.gencode(node.children[0])
                self.write_bin('send')

            case other:
                raise Exception('Generation failed!')
