VERIFIED_COMPONENTS = set(['Caixa de som', 'HD', 'SSD', 'Placa de vídeo', 
                               'Placa mãe', 'Processador', 'Memória RAM', 'Fonte', 
                               'Cooler', 'Gabinete', 'Monitor', 'Teclado', 
                               'Mouse', 'Cabo de energia', 'Cabo HDMI', 'Cabo USB', 
                               'Cabo de rede', 'Cabo VGA', 'Cabo DisplayPort', 'Cabo DVI'])

def create_report(defective_components) -> set:
    '''This function creates a report of verified and defective 
    components, and prints the components that can be sold.'''
    
    ok_components = VERIFIED_COMPONENTS.difference(defective_components)
    
    print(f'\nQuantidade de componentes verificados: {len(VERIFIED_COMPONENTS)}')
    print(f'Quantidade de componentes defeituosos: {len(defective_components)}')
    print(f'\nOs componentes que podem ser vendido são:')
    
    for component in ok_components:
        print(f'- {component}')
        
    return ok_components
    
if __name__ == "__main__":
    create_report(set(['Caixa de som', 'HD', 'SSD', 'Placa de vídeo',]))