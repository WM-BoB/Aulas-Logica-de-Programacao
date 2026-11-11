import matplotlib.pyplot as plt

# Dados
x = [1, 2, 3, 4, 5]
y = [2.33, 4.1, 1.5, 3.4, 4.5]

def plotar_grafico_linhas(x, y):
    # Criar um gráfico de linhas
    plt.plot(x, y, color='lightcoral')

    # Adicionar rótulos aos eixos
    plt.xlabel('Eixo X', fontsize=12, fontweight='bold', color='green')
    plt.ylabel('Eixo Y', fontsize=12, fontweight='bold', color='green')

    # Adicionar um título ao gráfico
    plt.title('Gráfico de Linhas', fontsize=20, fontweight='bold', color='red')

    # Mostrar o gráfico
    plt.show()
    
if __name__ == '__main__':
    plotar_grafico_linhas(x, y)
    