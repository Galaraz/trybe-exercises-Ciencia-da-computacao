from personagem_interface import PersonagemInterface


class Personagem(PersonagemInterface):
    """Criar modelo de Personagem"""
    def __init__(self, nome, especie, sexo, altura, peso):
        self.__nome = nome
        self.__especie = especie
        self.__sexo = sexo
        self.__altura = altura
        self.__peso = peso
   
    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def get_especie(self):
        return self.__especie

    def get_sexo(self):
        return self.__sexo

    def get_altura(self):
        return self.__altura

    def get_peso(self):
        return self.__peso