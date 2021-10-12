import twint
import os
import pandas as pd
from datetime import datetime
from datetime import timedelta
from pathlib import Path

# -----------------------------------------------------------------------#
# --------------------- Configurações para o Twint ----------------------#
# -----------------------------------------------------------------------#
def buscarHashtag(tag, data):

    #Setando a tag de busca
    hashTagOficial = tag

    #Setando as datas de busca
    dataEstreiaString = data
    dataEstreia = datetime.strptime(dataEstreiaString, '%Y-%m-%d')
    dataInicial = dataEstreia - timedelta(days=30)
    dataFinal = dataEstreia + timedelta(days=180)

    #Diretorio de Trabalho
    caminho_absoluto = os.path.dirname(os.path.realpath(__file__))
    caminho_base = f"{caminho_absoluto}/{hashTagOficial[1:]}/"

    if Path(caminho_base).is_dir():
        print("OK! Diretório: ", caminho_base, " é um diretorio existente")
    else:
        print("Diretório: ", caminho_base, " não é um diretorio existente.\nCriando o diretorio...")
        os.mkdir(caminho_base)
        print("Diretório: ", caminho_base, " criado com sucesso!")

    # 30 dias antes + 180 dias depois
    for i in range(0,10,5):
        dataS = ( dataInicial + timedelta(days=i) ).strftime("%Y-%m-%d")
        dataU = ( dataInicial + timedelta(days=i+5) ).strftime("%Y-%m-%d")

        #Arquivo de saída
        arquivoSaida = caminho_base + f"{i}" + ".csv"
        print(arquivoSaida)

        #Adicionar configurações
        config = twint.Config()
        config.Search = hashTagOficial
        config.Since = dataS
        config.Until = dataU
        config.Hide_output = True
        config.Count = True 
        config.Output = arquivoSaida

        #Executar a busca
        twint.run.Search(config)
        #Exibir na tela o progresso atual
        print(f"{hashTagOficial}. Fim do dia {i+1}. Data Inicial: {dataS} Data Final: {dataU}")


# -----------------------------------------------------------------------#
# ----------------------- Leitura de arquivo aqui -----------------------#
# -----------------------------------------------------------------------#
#tag = "#TheWitcher"
#data = '2019-12-20'
#data = '2019-01-20'

pd_series = pd.read_csv("input_twitter.csv")

tamSeries = pd_series.shape[0]
for i in range(tamSeries):
	tag = pd_series.loc[i, 'hashtag']
	data = pd_series.loc[i, 'data_lancamento']

	buscarHashtag(tag, data)
