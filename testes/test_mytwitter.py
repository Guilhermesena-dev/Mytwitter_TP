import sys
import os
import unittest

# Adiciona o diretório raiz ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.excecoes import PIException, PDException, PEException, MFPException, SIException
from src.mytwitter import MyTwitter, Tweet
from src.usuarios import PessoaFisica, PessoaJuridica
from src.perfil import Perfil

class TestMyTwitter(unittest.TestCase):
    def setUp(self):
        # Método executado antes de cada teste
        self.twitter = MyTwitter()
        self.usuario1 = PessoaFisica("@usuario1", "12345678900")
        self.usuario2 = PessoaJuridica("@empresa1", "12345678000199")
        self.twitter.criar_perfil(self.usuario1)
        self.twitter.criar_perfil(self.usuario2)

    def test_criar_usuario(self):
        # Testando a criação de um usuário.
        self.assertEqual(self.usuario1.get_usuario(), "@usuario1")
        self.assertEqual(self.usuario2.get_cnpj(), "12345678000199")
        # Verifica se o perfil está ativo por padrão.
        self.assertTrue(self.usuario1.is_ativo())
        self.assertTrue(self.usuario2.is_ativo())

    def test_cadastrar_usuario_existente(self):
        # Testando a tentativa de cadastrar um usuário já existente.
        with self.assertRaises(PEException) as context:
            self.twitter.criar_perfil(PessoaFisica("@usuario1", "11111111111"))
        self.assertEqual(str(context.exception), "Perfil já existe")

    def test_tweetar_e_timeline(self):
        # Testa a criação de tweets e a recuperação da timeline.
        self.twitter.tweetar("@usuario1", "Meu primeiro tweet!")
        self.twitter.tweetar("@usuario1", "Segundo tweet!")
        
        tweets = self.usuario1.get_tweets()
        self.assertEqual(len(tweets), 2)
        # Tweets mais recentes primeiro na lista de tweets
        self.assertEqual(tweets[0].get_mensagem(), "Segundo tweet!")
        self.assertEqual(tweets[1].get_mensagem(), "Meu primeiro tweet!")
        
        # Verifica se a timeline está correta (ordem cronológica: mais antigo primeiro)
        timeline = self.twitter.timeline("@usuario1")
        self.assertEqual(len(timeline), 2)
        self.assertEqual(timeline[0].get_mensagem(), "Meu primeiro tweet!")
        self.assertEqual(timeline[1].get_mensagem(), "Segundo tweet!")

    def test_cancelar_perfil(self):
        # Testa cancelar perfil inexistente.
        with self.assertRaises(PIException):
            self.twitter.cancelar_perfil("@usuario_inexistente")
        
        # Cria e cancela um perfil.
        perfil = PessoaFisica("@usuario3", "11111111111")
        self.twitter.criar_perfil(perfil)
        self.twitter.cancelar_perfil("@usuario3")
        # Verifica se o perfil foi desativado.
        self.assertFalse(perfil.is_ativo())
        
        # Tenta cancelar perfil já desativado.
        with self.assertRaises(PDException):
            self.twitter.cancelar_perfil("@usuario3")

    def test_perfil_inexistente(self):
        # Testa a tentativa de recuperar a timeline de um perfil inexistente.
        with self.assertRaises(PIException) as context:
            self.twitter.timeline("@usuarioInexistente")
        self.assertEqual(str(context.exception), "Perfil inexistente")

    def test_seguir_usuario(self):
        # Testa seguir outro usuário.
        self.twitter.seguir("@usuario1", "@empresa1")
        seguidores = self.twitter.seguidores("@empresa1")
        seguidos = self.twitter.seguidos("@usuario1")
        self.assertIn(self.usuario1, seguidores)
        self.assertIn(self.usuario2, seguidos)
    
if __name__ == '__main__':
    unittest.main()

