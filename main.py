from src.mytwitter import MyTwitter
from src.usuarios import PessoaFisica, PessoaJuridica
import time

def main():
    print("\n=== Bem-vindo ao MyTwitter! ===")
    twitter = MyTwitter()
    
    # criando perfis
    usuario1 = PessoaFisica("@usuario1", "12345678900")
    usuario2 = PessoaJuridica("@empresa1", "12345678000199")
    
    twitter.criar_perfil(usuario1)
    twitter.criar_perfil(usuario2)
    
    print(f"Perfil {usuario1.get_usuario()} criado com sucesso.")
    print(f"Perfil {usuario2.get_usuario()} criado com sucesso.\n")
    
    # usuário 1 faz tweets
    twitter.tweetar("@usuario1", "Meu primeiro tweet!")
    time.sleep(1)  # Simula tempo entre tweets
    twitter.tweetar("@usuario1", "Mais um dia aprendendo Python!")
    
    print(f"{usuario1.get_usuario()} tweetou: 'Meu primeiro tweet!'\n")
    print(f"{usuario1.get_usuario()} tweetou: 'Mais um dia aprendendo Python!'\n")
    
    # usuário 2 segue Usuário 1
    twitter.seguir("@empresa1", "@usuario1")
    print(f"{usuario2.get_usuario()} começou a seguir {usuario1.get_usuario()}\n")
    
    # exibir timeline do usuário 2
    print(f"Timeline de {usuario2.get_usuario()}:\n")
    for tweet in twitter.timeline("@empresa1"):
        print(f"{tweet.get_usuario()}: {tweet.get_mensagem()} - {tweet.get_data_postagem()}")
    
    # cancelar o perfil do usuário 1
    twitter.cancelar_perfil("@usuario1")
    print(f"Perfil {usuario1.get_usuario()} foi desativado.\n")
    
    # tentar tweetar com perfil desativado
    try:
        twitter.tweetar("@usuario1", "Tentando tweetar com conta desativada...")
    except Exception as e:
        print(f"Erro: {e}\n")

if __name__ == "__main__":
    main()