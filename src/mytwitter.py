from .excecoes import UJCException, UNCException, PIException, PDException, MFPException, PEException, SIException
from .perfil import *  # Módulo com a classe Perfil (supondo que você já a tenha)
from .RepositorioUsuarios import *  # Módulo com a classe RepositorioUsuarios
from datetime import datetime

class MyTwitter:
    def __init__(self):
        self.__repositorio = RepositorioUsuarios()
        
    def _validar_usuario(self, usuario):
        if not usuario.startswith('@'):
            usuario = '@' + usuario
        return usuario
    
    def criar_perfil(self, perfil):
        if self.__repositorio.buscar(perfil.get_usuario()) is not None:
            raise PEException("Perfil já existe")
        self.__repositorio.cadastrar(perfil)
    
    def cancelar_perfil(self, usuario):
        usuario = self._validar_usuario(usuario)
        perfil = self.__repositorio.buscar(usuario)
        if perfil is None:
            raise PIException("Perfil inexistente")
        if not perfil.is_ativo():
            raise PDException("Perfil já está desativado")
        perfil.set_ativo(False)
    
    def tweetar(self, usuario, mensagem):
        if len(mensagem) < 1 or len(mensagem) > 140:
            raise MFPException("Mensagem deve ter entre 1 e 140 caracteres")
        
        usuario = self._validar_usuario(usuario)
        perfil = self.__repositorio.buscar(usuario)
        if perfil is None:
            raise PIException("Perfil inexistente")
        if not perfil.is_ativo():
            raise PDException("Perfil está desativado")
            
        tweet = Tweet(usuario, mensagem)
        perfil.adicionar_tweet(tweet)
    
    def timeline(self, usuario):
        usuario = self._validar_usuario(usuario)
        perfil = self.__repositorio.buscar(usuario)
        if perfil is None:
            raise PIException("Perfil inexistente")
        if not perfil.is_ativo():
            raise PDException("Perfil está desativado")
        return perfil.get_timeline()
    
    def tweets(self, usuario):
        usuario = self._validar_usuario(usuario)
        perfil = self.__repositorio.buscar(usuario)
        if perfil is None:
            raise PIException("Perfil inexistente")
        if not perfil.is_ativo():
            raise PDException("Perfil está desativado")
        return perfil.get_tweets()
    
    def seguir(self, seguidor, seguido):
        seguidor = self._validar_usuario(seguidor)
        seguido = self._validar_usuario(seguido)
        
        if seguidor == seguido:
            raise SIException("Usuário não pode seguir a si mesmo")
            
        perfil_seguidor = self.__repositorio.buscar(seguidor)
        perfil_seguido = self.__repositorio.buscar(seguido)
        
        if perfil_seguidor is None or perfil_seguido is None:
            raise PIException("Perfil inexistente")
        if not perfil_seguidor.is_ativo() or not perfil_seguido.is_ativo():
            raise PDException("Perfil está desativado")
            
        perfil_seguidor.seguir(perfil_seguido)
        perfil_seguido.adicionar_seguidor(perfil_seguidor)
    
    def numero_seguidores(self, usuario):
        usuario = self._validar_usuario(usuario)
        perfil = self.__repositorio.buscar(usuario)
        if perfil is None:
            raise PIException("Perfil inexistente")
        if not perfil.is_ativo():
            raise PDException("Perfil está desativado")
            
        seguidores_ativos = [s for s in perfil.get_seguidores() if s.is_ativo()]
        return len(seguidores_ativos)
    
    def seguidores(self, usuario):
        usuario = self._validar_usuario(usuario)
        perfil = self.__repositorio.buscar(usuario)
        if perfil is None:
            raise PIException("Perfil inexistente")
        if not perfil.is_ativo():
            raise PDException("Perfil está desativado")
            
        return [s for s in perfil.get_seguidores() if s.is_ativo()]
    
    def seguidos(self, usuario):
        usuario = self._validar_usuario(usuario)
        perfil = self.__repositorio.buscar(usuario)
        if perfil is None:
            raise PIException("Perfil inexistente")
        if not perfil.is_ativo():
            raise PDException("Perfil está desativado")
            
        return [s for s in perfil.get_seguidos() if s.is_ativo()]

class Tweet:
    def __init__(self, usuario, mensagem):
        self.__usuario = usuario
        self.__mensagem = mensagem
        self.__data_postagem = datetime.now()
        self.__id = id(self)
    
    def get_usuario(self):
        """Retorna o nome do usuário que criou o tweet"""
        return self.__usuario
    
    def get_mensagem(self):
        """Retorna o conteúdo do tweet"""
        return self.__mensagem
    
    def get_data_postagem(self):
        return self.__data_postagem
    
    def get_id(self):
        return self.__id
