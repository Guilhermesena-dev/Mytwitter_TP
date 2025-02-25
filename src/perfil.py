from threading import Lock

class Perfil:
    def __init__(self, usuario):
        if not usuario.startswith('@'):
            raise ValueError("Nome de usuário deve começar com @")
        self.__usuario = usuario
        self.__seguidos = set()
        self.__seguidores = set()
        self.__tweets = []
        self.__ativo = True
        self.__lock = Lock()

    def adicionar_seguidor(self, perfil):
        self.__seguidores.add(perfil)

    def seguir(self, perfil):
        self.__seguidos.add(perfil)

    def adicionar_tweet(self, tweet):
        with self.__lock:
            self.__tweets.append(tweet)

    def get_tweets(self):
        with self.__lock:
            return list(reversed(self.__tweets))

    def get_tweet(self, tweet_id):
        with self.__lock:
            return next((t for t in self.__tweets if t.get_id() == tweet_id), None)

    def get_timeline(self):
        with self.__lock:
            timeline = self.__tweets.copy()
            for seguido in self.__seguidos:
                if seguido.is_ativo():
                    timeline.extend(seguido.get_tweets())
            return sorted(timeline, key=lambda t: t.get_data_postagem(), reverse=True)

    def get_usuario(self):
        return self.__usuario

    def set_ativo(self, ativo):
        self.__ativo = ativo

    def is_ativo(self):
        return self.__ativo
    
    def get_seguidores(self):
        return list(self.__seguidores)
    
    def get_seguidos(self):
        return list(self.__seguidos)
