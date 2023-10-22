from src.cLexer import Lexer


def run_lexer_last(lxr):
    while lxr.next():
        continue
    return lxr.last


# ================= TEST MAIN =====================

lexer = Lexer()


def test_eof():
    lexer.content = "je suis libertine"
    run_lexer_last(lexer)
    assert lexer.token == {'type': 'EOF'}


def test_const():
    lexer.content = '0'
    assert run_lexer_last(lexer) == {'type': 'const', 'value': '0'}
    lexer.content = '1 2'
    assert run_lexer_last(lexer) == {'type': 'const', 'value': '2'}


lexer.content = ""


def test_id():
    lexer.content = '123 3 voiture'
    assert run_lexer_last(lexer) == {'type': 'id', 'value': 'voiture'}


def test_full():
    lexer.content = 'int main(){int a; a=2; return a;}'
    lexer.next()
    assert lexer.check('int')
    assert lexer.check('id')
    assert lexer.check('(')
    assert lexer.check(')')
    assert lexer.check('{')
    assert lexer.check('int')
    assert lexer.check('id')
    assert lexer.check(';')
    assert lexer.check('id')
    assert lexer.check('=')
    assert lexer.token['value'] == '2' and lexer.check('const')
    assert lexer.check(';')
    assert lexer.check('return')
    assert lexer.check('id')
    assert lexer.check(';')
    assert lexer.check('}')
