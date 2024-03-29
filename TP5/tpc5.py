import ply.lex as lex
import json
import math

class StockSystem:
    def __init__(self):
        self.lista_produtos = self.carregar_estoque()
        self.saldo_atual = 0

    def carregar_estoque(self):
        try:
            with open("stock.json", 'r') as arquivo:
                lista_produtos = json.load(arquivo)
                return lista_produtos
        except FileNotFoundError:
            print("Arquivo stock.json não encontrado")
            return []


    def salvar_estoque(self):
        with open("stock.json", 'w') as arquivo:
            json.dump(self.lista_produtos, arquivo, indent=2)

    def obter_valor_moeda(self, moeda):
        for (moeda_val, valor) in moedas:
            if moeda == moeda_val:
                return valor
        return None

    def calcular_troco(self, valor):
        valor = round(valor, 2)
        moedas_dict = {}
        for (moeda, valor_moeda) in moedas:
            while valor >= valor_moeda:
                moedas_dict[moeda] = moedas_dict.get(moeda, 0) + 1
                valor = round(valor - valor_moeda, 2)
        troco_str = "Pode retirar o troco: "
        first = True
        for value, number in moedas_dict.items():
            if first:
                troco_str += f"{number}x {value}"
                first = False
            else:
                troco_str += f", {number}x {value}"
        troco_str += "."
        return troco_str

    def valor_para_moedas(self, valor):
        parte_fracionaria, parte_inteira = math.modf(valor)
        result_str = ""
        if parte_inteira > 0:
            result_str += f"{int(parte_inteira)}e"
        if parte_fracionaria > 0:
            result_str += f"{int(round(parte_fracionaria * 100, 0))}c"
        if not result_str:
            result_str = "0"
        return result_str

    def listar_produtos(self):
        print("""cod | nome | quantidade | preço
---------------------------------""")
        for produto in self.lista_produtos:
            print(f"{produto['cod']} {produto['nome']} {produto['quant']} {produto['preco']}")

    def depositar_moedas(self, entrada):
        sair = False
        while not sair:
            token = next(entrada)
            if token.type == 'PONTO':
                break
            elif token.type == 'MOEDA':
                valor_moeda = self.obter_valor_moeda(token.value)
                if valor_moeda is not None:
                    self.saldo_atual += valor_moeda
                else:
                    print("O valor inserido não corresponde a uma moeda válida")
            elif token.type == 'VIRGULA':
                pass
            else:
                print("Input inválido")
        print(f"Saldo = {self.valor_para_moedas(self.saldo_atual)}")

    def selecionar_produto(self, entrada):
        token = next(entrada, None)
        if token and token.type == 'ID':
            for produto in self.lista_produtos:
                if produto['cod'] == token.value:
                    if self.saldo_atual >= produto['preco']:
                        self.saldo_atual -= produto['preco']
                        produto['quant'] -= 1
                        print(f"Pode retirar o produto dispensado {produto['nome']}")
                        print(f"Saldo = {self.valor_para_moedas(self.saldo_atual)}")
                    else:
                        print("Saldo insuficiente para satisfazer o seu pedido")
                        print(f"Saldo = {self.valor_para_moedas(self.saldo_atual)}; Pedido = {self.valor_para_moedas(produto['preco'])}")
                    break
            else:
                print("O artigo selecionado não existe")
        else:
            print("Input inválido")

    def executar_comando(self, entrada):
        for token in entrada:
            if token.type == 'SAIR':
                return False
            elif token.type == 'LISTAR':
                self.listar_produtos()
            elif token.type == 'DEPOSITAR':
                self.depositar_moedas(entrada)
            elif token.type == 'SELECIONAR':
                self.selecionar_produto(entrada)
            else:
                print("Input inválido")
        return True

# Definindo as moedas
moedas = [("2e", 2), ("1e", 1), ("50c", 0.50), ("20c", 0.20), ("10c", 0.10), ("5c", 0.05), ("2c", 0.02), ("1c", 0.01)]

# Definindo o lexer
tokens = (
    'LISTAR',
    'DEPOSITAR',
    'SELECIONAR',
    'SAIR',
    'VIRGULA',
    'PONTO',
    'MOEDA',
    'ID'
)

t_LISTAR = r'LISTAR'
t_DEPOSITAR = r'MOEDA'
t_SELECIONAR = r'SELECIONAR'
t_SAIR = r'SAIR'
t_VIRGULA = r','
t_PONTO = r'\.'

def t_MOEDA(t):
    r'\d+(e|c)'
    return t

def t_ID(t):
    r'[A-Z]\d{2}'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

def main():
    
    print("Stock carregado, Estado atualizado.")
    print("Bom dia. Estou disponível para atender o seu pedido.")

    continuar = True
    sistema = StockSystem()

    while continuar:
        entrada = input(">> ")
        lexer.input(entrada)
        continuar = sistema.executar_comando(lexer)
    
    if sistema.saldo_atual > 0:
        print(sistema.calcular_troco(sistema.saldo_atual))
    else:
        print("Não há troco para ser devolvido")
    
    sistema.salvar_estoque()
    print("Até à próxima")

if __name__ == "__main__":
    main()