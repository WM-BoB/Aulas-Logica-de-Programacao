from create_report import create_report

def test_create_report():
    defective_components = set(['HD', 'SSD', 'Placa de vídeo'])
    expected_ok_components = set(['Caixa de som', 'Placa mãe', 'Processador', 
                                  'Memória RAM', 'Fonte', 'Cooler', 'Gabinete', 
                                  'Monitor', 'Teclado', 'Mouse', 'Cabo de energia', 
                                  'Cabo HDMI', 'Cabo USB', 'Cabo de rede', 
                                  'Cabo VGA', 'Cabo DisplayPort', 'Cabo DVI'])
    
    assert create_report(defective_components) == expected_ok_components