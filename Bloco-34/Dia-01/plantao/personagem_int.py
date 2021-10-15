from abc import ABCMeta


class PersonagemInterface(metaclass=ABCMeta):

    def get_nome(self):
        raise NotImplementedError

    def set_nome(self):
        raise NotImplementedError

    def get_especie(self):
        raise NotImplementedError

    def get_sexo(self):
        raise NotImplementedError

    def get_altura(self):
        raise NotImplementedError

    def get_peso(self):
        raise NotImplementedError
