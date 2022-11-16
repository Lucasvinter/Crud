import MySQLdb

class Conexao:
    def __init__(self):
        self.conn = MySQLdb.connect(
            host = '',
            database = '',
            user = '',
            password = '' 
        )
        self.cursor = self.conn.cursor()