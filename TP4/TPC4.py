from ply import lex

# Definição dos tokens
tokens = (
    'SELECT', 'FROM', 'WHERE', 'DELIMITER1', 'DELIMITER2',
    'ATTRIBUTE', 'NUMBER', 'OPERATOR'
)

# Regras para tokens simples
t_DELIMITER1 = r','
t_DELIMITER2 = r';'

# Regra para operadores
t_OPERATOR = r'[<>]=?|='

# Palavras reservadas (case insensitive)
reserved_words = {'SELECT', 'FROM', 'WHERE'}

# Regra para identificar palavras reservadas
def t_ATTRIBUTE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*|\*'
    if t.value.upper() in reserved_words:
        t.type = t.value.upper()
    return t

# Regra para números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regra para lidar com caracteres ignorados (por exemplo, espaços em branco)
t_ignore = ' \t'

# Regra para lidar com quebras de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Regra para lidar com erros
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)

# Construção do analisador léxico
lexer = lex.lex()

# Exemplo de uso
codigo = "select id, nome, *, salario FROM empregados WHERE salario >= 820;"
lexer.input(codigo)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)