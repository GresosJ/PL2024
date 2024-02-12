# TPC 1 - Análise de um Dataset
## Autor
 - A88000;
 - Gerson Henrique de Araújo Júnior;

## Enunciado
 - Proibido usar o módulo CSV;
 - Ler o dataset, processá-lo e criar os seguintes resultados: 
   - Lista ordenada alfabeticamente das modalidades desportivas;
   - Percentagens de atletas aptos e inaptos para a prática desportiva;
   - Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39], ...;

## Analise
Comecei por fazer parse do svg, e so guardo as informações das colunas modalidade, idade e resultado (8,5 12).

```python
    dados = {'modalidades': [], 'aptos': 0, 'inaptos': 0, 'faixas_etarias': {}}

        for linha in linhas:
            campos = linha.strip().split(',')

            # Verificar se há dados suficientes na linha
            if len(campos) >= 13:
                modalidade = campos[8]
                idade = int(campos[5])
                aptidao = campos[12].lower()
```

### Lista ordenada alfabeticamente das modalidades desportivas
Depois de ler o dataset, criei uma lista de modalidades, e adicionei a modalidade à lista, se ainda não estiver presente. No final, ordenei a lista de modalidades alfabeticamente.

```python
    # Adicionar modalidade à lista, se ainda não estiver presente
    if modalidade not in dados['modalidades']:
        dados['modalidades'].append(modalidade)
    # (...)
    # Ordenar a lista de modalidades alfabeticamente
        dados['modalidades'] = sorted(dados['modalidades'])
```

**Resultados** 
```bash
    Lista ordenada alfabeticamente das modalidades desportivas:
    ['Andebol', 'Atletismo', 'BTT', 'Badminton', 'Basquetebol', 'Ciclismo', 'Dança', 'Equitação', 'Esgrima', 'Futebol', 'Karaté', 'Orientação', 'Parapente', 'Patinagem', 'Triatlo']
```

### Percentagens de atletas aptos e inaptos para a prática desportiva
Depois de ler o dataset, contei o número de atletas aptos e inaptos para a prática desportiva.

```python
    # Contar atletas aptos e inaptos
    if aptidao == 'true':
        dados['aptos'] += 1
    elif aptidao == 'false':
        dados['inaptos'] += 1
```

Depois calculo as percentagens de atletas aptos e inaptos para a prática desportiva.

```python
    percentagem_aptos = (resultados['aptos'] / total_atletas) * 100
    percentagem_inaptos = (resultados['inaptos'] / total_atletas) * 100

    print("\nPercentagens de atletas aptos e inaptos para a prática desportiva:")
    print(f"Aptos: {percentagem_aptos:.2f}%")
    print(f"Inaptos: {percentagem_inaptos:.2f}%")
```

**Resultados**
```bash
    Percentagens de atletas aptos e inaptos para a prática desportiva:
    Aptos: 54.00%
    Inaptos: 46.00%
```
### Distribuição de atletas por escalão etário
Depois de ler o dataset, armazenei a distribuição de atletas por escalão etário. Para cada atleta, determinei a faixa etária e atualizei o dicionário correspondente.

```python
    # Determinar a faixa etária e atualizar o dicionário correspondente
    faixa_etaria = (idade // 5) * 5
    if faixa_etaria not in dados['faixas_etarias']:
        dados['faixas_etarias'][faixa_etaria] = 1
    else:
        dados['faixas_etarias'][faixa_etaria] += 1
```
**Resultados**
```bash
    Distribuição de atletas por escalão etário (intervalo de 5 anos):
    [20-24]: 80 atletas
    [25-29]: 102 atletas
    [30-34]: 104 atletas
    [35-39]: 14 atletas
```