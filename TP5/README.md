# TPC4: Analisador Léxico

## Autor
 - A88000;
 - Gerson Henrique de Araújo Júnior;

## Resolução
Este programa pretende simular o funcionamento de uma máquina de venda automática. O utilizador pode carregar o stock, listar os produtos disponíveis, selecionar um produto e sair da máquina. O utilizador pode também carregar a máquina com moedas.

Como podemos ver no exemplo a baixo:

```
Stock carregado, Estado atualizado.
Bom dia. Estou disponível para atender o seu pedido.
>> MOEDA 1e, 20c.
Saldo = 1e20c
>> LISTAR
cod | nome | quantidade | preço
---------------------------------
A23 água 0.5L 8 0.55
B12 refrigerante lata 15 0.9
C45 kinder bueno 20 0.9
D67 redbull 10 1.0
E89 bolacha 25 0.5
F34 sorvete de chocolate 5 2.0
G56 bolacha de agua e sal 30 0.3
H78 agua com gas 0.5L 12 0.6
I90 m&ms 18 0.7
J11 kinder delice 7 0.7
>> SELECIONAR J11
Pode retirar o produto dispensado kinder delice
Saldo = 50c
>> LISTAR
cod | nome | quantidade | preço
---------------------------------
A23 água 0.5L 8 0.55
B12 refrigerante lata 15 0.9
C45 kinder bueno 20 0.9
D67 redbull 10 1.0
E89 bolacha 25 0.5
F34 sorvete de chocolate 5 2.0
G56 bolacha de agua e sal 30 0.3
H78 agua com gas 0.5L 12 0.6
I90 m&ms 18 0.7
J11 kinder delice 6 0.7
>> SAIR
Pode retirar o troco: 1x 50c.
Até à próxima
```

O estado da maquina esta guardado num ficheiro de texto chamado "stock.json". Este ficheiro é carregado no inicio do programa e atualizado sempre que o utilizador carrega o stock ou retira um produto.