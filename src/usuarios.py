from .perfil import Perfil

class PessoaFisica(Perfil):
    def __init__(self, usuario, cpf):
        super().__init__(usuario)
        self.__cpf = cpf

    def get_cpf(self):
        return self.__cpf

class PessoaJuridica(Perfil):
    def __init__(self, usuario, cnpj):
        super().__init__(usuario)
        self.__cnpj = cnpj

    def get_cnpj(self):
        return self.__cnpj