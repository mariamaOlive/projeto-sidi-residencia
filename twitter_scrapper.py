from datetime import datetime
from datetime import timedelta
from pathlib import Path
import twint
import os
import time
import pandas as pd

#import de outros arquivos
from twitter_files import finalizacao_scrapping

# -----------------------------------------------------------------------#
# --------------------- Configurações para o Twint ----------------------#
# -----------------------------------------------------------------------# 
def buscarHashtag(tag, data):

    #Setando a tag de busca
    hashTagOficial = tag

    #Setando as datas de busca
    dataEstreiaString = data
    dataEstreia = datetime.strptime(dataEstreiaString, '%Y-%m-%d')
    dataInicial = dataEstreia - timedelta(days=75)
    dataFinal = dataEstreia + timedelta(days=150)

    #Diretorio de Trabalho
    caminho_absoluto = os.path.dirname(os.path.realpath(__file__))
    caminho_base = f"{caminho_absoluto}/{hashTagOficial[1:]}/"

    if Path(caminho_base).is_dir():
        print("OK! Diretório: ", caminho_base, " é um diretorio existente")
    else:
        print("Diretório: ", caminho_base, " não é um diretorio existente.\nCriando o diretorio...")
        os.mkdir(caminho_base)
        print("Diretório: ", caminho_base, " criado com sucesso!")

    # 75 dias antes + 155 dias depois
    for i in range(0,230,5):

        # Caso a coleta dê erro troque o valor da variavel abaixo "erro"
        # pelo numero do arquivo csv que deu erro
        # Exemplo: deu erro enquanto baixava o arquivo "20.csv",
        #          APAGUE o arquivo 20.csv da pasta e então coloque abaixo: erro = 20 
        erro = 0
        
        if i < erro:
            continue

        dataS = ( dataInicial + timedelta(days=i) ).strftime("%Y-%m-%d")
        dataU = ( dataInicial + timedelta(days=i+6) ).strftime("%Y-%m-%d")

        #Arquivo de saída
        arquivoSaida = caminho_base + f"{i}" + ".csv"
        print(arquivoSaida)

        flag_while = True
        while flag_while == True:
            try:
                #Adicionar configurações
                config = twint.Config()
                config.Search = hashTagOficial
                config.Since = dataS
                config.Until = dataU
                config.Hide_output = True
                config.Count = True 
                config.Store_csv = True
                config.Output = arquivoSaida

                #Executar a busca
                twint.run.Search(config)
                #Exibir na tela o progresso atual
                print(f"{hashTagOficial}. Fim do dia {i+1}. Data Inicial: {dataS} Data Final: {dataU}")
                flag_while = False
            except:
                print(f"\n\n\nERRO no arquivo {i}.csv    Apagando...")
                os.remove(arquivoSaida)
                time.sleep(8) #dorme por 8 segundos
                print(f"Arquivo {i}. Apagado!\n Baixando o arquivo {i}.csv novamente...\n\n\n")

    finalizacao_scrapping(caminho_absoluto, caminho_base, hashTagOficial[1:])

# -----------------------------------------------------------------------#
# ----------------------- Leitura de arquivo aqui -----------------------#
# -----------------------------------------------------------------------#
#tag = "#TheWitcher"
#data = '2019-12-20'
#data = '2019-01-20'
if __name__ == '__main__':
    pd_series = pd.read_csv("input_twitter.csv")

    tamSeries = pd_series.shape[0]
    for i in range(tamSeries):
        tag = pd_series.loc[i, 'hashtag']
        data = pd_series.loc[i, 'data_lancamento']

        buscarHashtag(tag, data)
