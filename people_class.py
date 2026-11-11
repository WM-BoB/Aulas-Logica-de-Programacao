class Pessoa:
    def __init__(self, nome, idade, genero, cidade):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.cidade = cidade
        
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Gênero: {self.genero}"

    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome}."
    
    def apresentação(self):
        return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e moro em {self.cidade}."
    
    def aniversario(self):
        self.idade += 1
        return f"Feliz aniversário {self.nome}! Agora você tem {self.idade} anos."
    
class Aluno(Pessoa):
    def __init__(self, nome, idade, genero, cidade, curso):
        super().__init__(nome, idade, genero, cidade)
        self.curso = curso
        
    def apresentar_aluno(self):
        return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos, moro em {self.cidade} e estou no curso de {self.curso}."
    
aluno = Aluno("João", 30, "Masculino", "Guarulhos", "Análise de Sistemas")
aluno2 = Aluno("Maria", 22, "Feminino", "Arujá", "Enfermagem")
print(aluno.apresentar_aluno())
print(aluno2.apresentar_aluno())
