import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def read_data():
    file_path = '/Users/weslleymatos/Downloads/airtravel.csv'
    data = pd.read_csv(file_path)
    data.columns = data.columns.str.strip().str.strip('"')
    return data

def data_details():
    data = read_data()
    print('Tipo: ', type(data))
    print('Quantidade de linhas: ', len(data))
    print('Quantidade de colunas: ', len(data.columns))
    print('Tipos dos indíces: ', data.dtypes)
    print('\n')
    print(data.head(n=5))
    print('\n')
    print(data.loc[6].values)

def plot_line_graph(data):
    plt.plot(data['Month'], data['1960'])
    plt.xlabel('Meses')
    plt.ylabel('Quantidade de passageiros')
    plt.title('Quantidade de passageiros por mês')
    plt.show()    
    
def plot_bar_graph(data):
    x = np.arange(len(data['Month']))
    largura = 0.25

    # Plotagem do gráfico de barras
    # Cada barra representa um ano
    plt.bar(x - largura, data['1958'], largura, label='1958')
    plt.bar(x, data['1959'], largura, label='1959')
    plt.bar(x + largura, data['1960'], largura, label='1960')
    plt.xticks(x, data['Month'])
    
    # Adicionar rótulos aos eixos
    plt.ylabel('Quantidade de passageiros')
    plt.xlabel('Meses')
    
    # Adicionar um título ao gráfico
    plt.title('Quantidade de passageiros por mês')
    
    # Adicionar legenda ao gráfico
    plt.legend()
    
    # Mostrar o gráfico
    plt.show()
    
if __name__ == "__main__":
    plot_bar_graph(read_data())