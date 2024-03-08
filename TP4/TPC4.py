from ply import lex

tokens = (
    'SELECT', 'FROM', 'WHERE', 'DELIMITER1', 'DELIMITER2',
    'ATTRIBUTE', 'NUMBER', 'OPERATOR'
)

t_DELIMITER1 = r','
t_DELIMITER2 = r';'
t_OPERATOR = r'[<>]=?|='

# Palavras reservadas (case insensitive)
reserved_words = {'SELECT', 'FROM', 'WHERE'}

def t_ATTRIBUTE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*|\*'
    if t.value.upper() in reserved_words:
        t.type = t.value.upper()
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)
    
def main():
    lexer = lex.lex()
    codigo = "select id, nome, *, salario FROM empregados WHERE salario >= 820;"
    lexer.input(codigo)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

if __name__ == "__main__":
    main()