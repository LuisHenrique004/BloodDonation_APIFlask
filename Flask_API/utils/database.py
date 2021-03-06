import psycopg2


class ConnectSingletonDB:
    _instance = None

    def __init__(self):
        self._connect = psycopg2.connect(
            host="localhost",
            database="projeto_doacao_sangue",
            user="postgres",
            password="0990"
        )

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def connect(self):
        return self._connect
