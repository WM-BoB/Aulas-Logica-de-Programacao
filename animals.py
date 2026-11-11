class Animal():
    def __init__(self, nome):
        self.nome = nome
    
    def barulho(self):
        pass
    
class Cachorro(Animal):
    def barulho(self):
        return "Au Au!"
    
class CachorroPolicia(Cachorro):
    def farofar(self):
        return f"O {self.nome} encontrou a pista e fez {self.barulho()}!"    
    
class Gato(Animal):
    def barulho(self):
        return "Miau!"
    
cachorro = Cachorro("Rex")
cachorro_policia = CachorroPolicia("Thor")
gato = Gato("Lua")

print(f"O cachorro {cachorro.nome} faz {cachorro.barulho()}")
print(cachorro_policia.farofar())
print(f"O gato {gato.nome} faz {gato.barulho()}")