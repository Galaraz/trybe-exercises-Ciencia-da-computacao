from personagem import Personagem
from light_saber import Light_Saber


class Jedi(Personagem):
    """Modela um Jedi"""

    def __init__(self, nome, especie, sexo, altura, peso):
        super().__init__(nome, especie, sexo, altura, peso)
    # Compor
        self.light_saber = Light_Saber("verde")

    def isjedi(self):
        self.jedi = True
        return self.jedi


class Sith(Jedi):
    def __init__(self, nome, especie, sexo, altura, peso):
        super().__init__(nome, especie, sexo, altura, peso)
    # Compor
        self.light_saber = Light_Saber("vermelho")

    # Sobrescreve o Método
    def isjedi(self):
        self.jedi = False
        return self.jedi