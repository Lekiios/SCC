from src.cLexer import Lexer


def run_lexer_last(lxr):
    while lxr.next():
        continue
    return lxr.last


# ================= TEST MAIN =====================
lexer = Lexer()


def test_const():
    lexer.content = '0'
    assert run_lexer_last(lexer) == {'type': 'const', 'value': '0'}
    lexer.content = '1 2'
    assert run_lexer_last(lexer) == {'type': 'const', 'value': '2'}
