import sqlite3

conn = sqlite3.connect('aulaDB.db')

def create_table(cursor):
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS alunos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        serie INTEGER,
                        cod_disciplina VARCHAR(5) NOT NULL,
                        nota REAL,
                        data DATE NOT NULL
                        );
                ''')
    print("Tabela criada com sucesso!")

def insert_data(cursor, nome, serie, cod_disciplina, nota, data):
    cursor.execute(f'''
                INSERT INTO alunos (nome, serie, cod_disciplina, nota, data)
                VALUES ('{nome}', {serie}, '{cod_disciplina}', {nota}, '{data}');
                ''')
    print("Dados inseridos com sucesso!")
    conn.commit()
    
def update_data(cursor, id, nome, serie, cod_disciplina, nota, data):
    cursor.execute(f'''
                UPDATE alunos
                SET nome = '{nome}', serie = {serie}, cod_disciplina = '{cod_disciplina}', nota = {nota}, data = '{data}'
                WHERE id = {id};
                ''')
    print("Dados atualizados com sucesso!")
    conn.commit()
    
def delete_data(cursor, id):
    cursor.execute(f'''
                DELETE FROM alunos
                WHERE id = {id};
                ''')
    print("Dados deletados com sucesso!")
    conn.commit()
    
def select_data(cursor):
    cursor.execute('''
                SELECT * FROM alunos;
                ''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

if __name__ == '__main__':
    cursor = conn.cursor()
    option = 0
    while option != "6":
        option = input('''---- CRUD SQLITE ----\n1 - Criar tabela\n2 - Inserir dados\n3 - Atualizar dados\n4 - Deletar dados\n5 - Selecionar dados\n6 - Sair\nSelecione uma opção: ''')
        print()
        match option:
            case "1":
                create_table(cursor)
            case "2":
                nome = input("Digite o nome do aluno:")
                serie = int(input("Digite a série do aluno:"))
                cod_disciplina = input("Digite o código da disciplina:")
                nota = float(input("Digite a nota do aluno:"))
                data = input("Digite a data (YYYY-MM-DD):")
                insert_data(cursor, nome, serie, cod_disciplina, nota, data)
            case "3":
                id = int(input("Digite o ID do aluno a ser atualizado:"))
                nome = input("Digite o novo nome do aluno:")
                serie = int(input("Digite a nova série do aluno:"))
                cod_disciplina = input("Digite o novo código da disciplina:")
                nota = float(input("Digite a nova nota do aluno:"))
                data = input("Digite a nova data (DD/MM/YYYY):")
                update_data(cursor, id, nome, serie, cod_disciplina, nota, data)
            case "4":
                id = int(input("Digite o ID do aluno a ser deletado:"))
                delete_data(cursor, id)
            case "5":
                select_data(cursor)
            case "6":
                print("Saindo do programa...")
            case _:
                print("Opção inválida!")
        print()
    conn.close()