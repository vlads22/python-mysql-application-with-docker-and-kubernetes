import MySQLdb


class MySQL:
    def __init__(self, host, port, user, passwd, database):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.database = database
        self.db = MySQLdb.connect(host=self.host, port=self.port, user=self.user,
                                  passwd=self.passwd, database=self.database)
        self.cursor = self.db.cursor()

    def execute(self, query, record=""):
        self.cursor.execute(query, record)
        result = self.cursor.fetchall()
        self.db.commit()
        list_response = [list(index) for index in result]
        return list_response

    def close(self):
        self.db.close()
