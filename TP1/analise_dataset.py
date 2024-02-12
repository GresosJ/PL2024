# Função para ler o arquivo e processar os dados
def processar_dataset(arquivo):
    with open(arquivo, 'r') as file:
        linhas = file.readlines()

        # Remover cabeçalho, se existir
        header = linhas[0].strip().split(',')
        linhas = linhas[1:]

        # Dicionário para armazenar os dados processados
        dados = {'modalidades': [], 'aptos': 0, 'inaptos': 0, 'faixas_etarias': {}}

        for linha in linhas:
            campos = linha.strip().split(',')

            # Verificar se há dados suficientes na linha
            if len(campos) >= 13:
                modalidade = campos[8]
                idade = int(campos[5])
                aptidao = campos[12].lower()

                # Adicionar modalidade à lista, se ainda não estiver presente
                if modalidade not in dados['modalidades']:
                    dados['modalidades'].append(modalidade)

                # Contar atletas aptos e inaptos
                if aptidao == 'true':
                    dados['aptos'] += 1
                elif aptidao == 'false':
                    dados['inaptos'] += 1

                # Determinar a faixa etária e atualizar o dicionário correspondente
                faixa_etaria = (idade // 5) * 5
                if faixa_etaria not in dados['faixas_etarias']:
                    dados['faixas_etarias'][faixa_etaria] = 1
                else:
                    dados['faixas_etarias'][faixa_etaria] += 1

        # Ordenar a lista de modalidades alfabeticamente
        dados['modalidades'] = sorted(dados['modalidades'])

        return dados

# Nome do arquivo do dataset
nome_arquivo = 'emd.csv'

# Processar o dataset
resultados = processar_dataset(nome_arquivo)

# Imprimir os resultados
print("Lista ordenada alfabeticamente das modalidades desportivas:")
print(resultados['modalidades'])

total_atletas = resultados['aptos'] + resultados['inaptos']

# Verificar se o total de atletas é zero antes de calcular as percentagens
if total_atletas != 0:
    percentagem_aptos = (resultados['aptos'] / total_atletas) * 100
    percentagem_inaptos = (resultados['inaptos'] / total_atletas) * 100

    print("\nPercentagens de atletas aptos e inaptos para a prática desportiva:")
    print(f"Aptos: {percentagem_aptos:.2f}%")
    print(f"Inaptos: {percentagem_inaptos:.2f}%")

    print("\nDistribuição de atletas por escalão etário (intervalo de 5 anos):")
    for faixa_etaria, quantidade in sorted(resultados['faixas_etarias'].items()):
        print(f"[{faixa_etaria}-{faixa_etaria + 4}]: {quantidade} atletas")
else:
    print("\nNão há atletas no dataset.")
