# TPC4: Analisador Léxico

## Autor
 - A88000;
 - Gerson Henrique de Araújo Júnior;

## Enunciado
Construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases do género:

```mysql
Select id, nome, salario From empregados Where salario >= 820
```

## Resolução
Para isto foi criado um programa em python que lê um ficheiro de texto e devolve os tokens que o compõem. Para tal, foi criada uma função que lê o ficheiro e devolve uma lista com os tokens. Esta função lê o ficheiro e, para cada linha, separa as palavras e verifica se estas são palavras reservadas, identificadores, números ou símbolos. Caso sejam, adiciona-os à lista de tokens. Caso contrário, devolve um erro.