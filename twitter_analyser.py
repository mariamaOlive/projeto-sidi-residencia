import pandas as pd
import os
from pathlib import Path

def juntarSeries(caminho_serie, nome_serie):
    
    lista_arq = []
    for i in range(0,395,5):
        lista_arq.append(f"{i}" + ".csv")
        
    lista_df = []
    print(f"Lista_arq: {lista_arq}")
    for nome_arquivo in lista_arq:
        # print(f"Lista_arq: {nome_arquivo}")
        
        caminho_arquivo = caminho_serie + nome_arquivo
        #print(caminho_arquivo)
        meuArquivo = open(caminho_arquivo, 'r', encoding="utf-8")
        meuArquivo.read()
        #df_arquivo = pd.read_csv(caminho_arquivo, header=None, delim_whitespace=True)
        df_arquivo = pd.read_csv(caminho_arquivo, delimiter='·',
                   engine = 'python')
        lista_df.append(df_arquivo)

    df_final = pd.concat(lista_df)
    print(df_final.head())
    print(df_final.columns)
    #df_final.to_csv(f"{caminho_serie}{nome_serie}.csv", index = False, header=True)


if __name__ == '__main__':
    caminho_absoluto = os.path.dirname(os.path.realpath(__file__))
    #print(caminho_absoluto)
    caminho_relativo = caminho_absoluto + '/series_dataset'
    #print(caminho_relativo)

    cont = 0
    for dir in os.listdir(Path(caminho_relativo)):

        if dir == 'Ozark': #or dir == 'SexEducation' or dir == 'StrangerThings' or dir == 'TheWitcher':
            #print(dir)

            caminho_serie = f"{caminho_relativo}/{dir}/"
            print(caminho_serie)

            juntarSeries(caminho_serie, dir)