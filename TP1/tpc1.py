def processar_dataset(arquivo):
    with open(arquivo, 'r') as file:
        linhas = file.readlines()

        header = linhas[0].strip().split(',')
        linhas = linhas[1:]

        dados = {'modalidades': [], 'aptos': 0, 'inaptos': 0, 'faixas_etarias': {}}

        for linha in linhas:
            campos = linha.strip().split(',')

            if len(campos) >= 13:
                modalidade = campos[8]
                idade = int(campos[5])
                aptidao = campos[12].lower()

                if modalidade not in dados['modalidades']:
                    dados['modalidades'].append(modalidade)

                if aptidao == 'true':
                    dados['aptos'] += 1
                elif aptidao == 'false':
                    dados['inaptos'] += 1

                faixa_etaria = (idade // 5) * 5
                if faixa_etaria not in dados['faixas_etarias']:
                    dados['faixas_etarias'][faixa_etaria] = 1
                else:
                    dados['faixas_etarias'][faixa_etaria] += 1

        dados['modalidades'] = sorted(dados['modalidades'])

        return dados

nome_arquivo = 'emd.csv'

resultados = processar_dataset(nome_arquivo)

print("Lista ordenada alfabeticamente das modalidades desportivas:")
print(resultados['modalidades'])

total_atletas = resultados['aptos'] + resultados['inaptos']

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