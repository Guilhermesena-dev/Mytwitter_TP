from .perfil import *
from .excecoes import *


class RepositorioUsuarios:
    def __init__(self):
        self.__usuarios = {}

    def cadastrar(self, usuario):
        if self.buscar(usuario.get_usuario()) is not None:
            raise UJCException(f"Usuário {usuario.get_usuario()} já está cadastrado!")
        self.__usuarios[usuario.get_usuario()] = usuario

    def buscar(self, usuario):
        return self.__usuarios.get(usuario)

    def atualizar(self, usuario):
        if usuario.get_usuario() not in self.__usuarios:
            raise UNCException(f"Usuário {usuario.get_usuario()} não está cadastrado")
        self.__usuarios[usuario.get_usuario()] = usuario