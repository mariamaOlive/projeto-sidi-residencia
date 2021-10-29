import pandas as pd
import os
from pathlib import Path

def juntar_series(caminho_relativo, caminho_serie, nome_serie):
    
    lista_arq = []
    for i in range(225,-1,-5):
        lista_arq.append(f"{i}" + ".csv")
    
    lista_df = []
    for nome_arquivo in lista_arq:
        caminho_arquivo = caminho_serie + nome_arquivo

        lista_arquivos = os.listdir(Path(caminho_serie))
        if nome_arquivo in lista_arquivos:
            df_arquivo = pd.read_csv(caminho_arquivo)
            lista_df.append(df_arquivo)

    df_final = pd.concat(lista_df)
    print(f"Head:\n{df_final['date'].head(5)}")
    print(f"Tail:\n{df_final['date'].tail(5)}")
    print(df_final.columns)
    df_final.to_csv(f"{caminho_relativo}{nome_serie}.csv", index = False, header=True)


def finalizacao_scrapping(caminho_absoluto, caminho_base, nome):
    caminho_relativo = caminho_absoluto + '/series_dataset/'

    if Path(caminho_relativo).is_dir():
        print("OK! Diretório: ", caminho_relativo, " é um diretorio existente")
    else:
        print("Diretório: ", caminho_relativo, " não é um diretorio existente.\nCriando o diretorio...")
        os.mkdir(caminho_relativo)
        print("Diretório: ", caminho_relativo, " criado com sucesso!")

    juntar_series(caminho_relativo, caminho_base, nome)