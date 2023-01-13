import pandas as pd

# Coloque o nome do arquivo com os dados exportados na mesma pasta que este script 
# e insira o nome abaixo entre parenteses.
Data = pd.read_json('./nome_documento_com_dados_exportados.json')

index = 0
for annotation in Data.Label:
    if annotation['classifications'] == []:
        Data.drop(index, inplace=True)
    index += 1

Data.reset_index(inplace=True)
Data.drop(columns=['index'], inplace=True)

# Coloque o nome desejado para o arquivo destino csv abaixo entre parenteses 
Data.to_csv("nome_documento_sem_anotacoes_vazias.csv")
