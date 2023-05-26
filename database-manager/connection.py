import MySQLdb
import logging
import time
import traceback

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


def establish_db_connection(config):
    db_connection_hardware = ""
    i = 1
    while i < 10:
        try:
            logging.info("config.DB_HARDWARE.PASSWORD: %s", config.DB_HARDWARE.PASSWORD) 
            logging.info("config.DB_HARDWARE_PORT: %s", config.DB_HARDWARE.PORT) 
            db_connection_hardware = MySQL(host=config.DB_HARDWARE.HOST, port=config.DB_HARDWARE.PORT,
                                user=config.DB_HARDWARE.USER, passwd=config.DB_HARDWARE.PASSWORD, database=config.DB_HARDWARE.DATABASE)
            logging.info("DB connection succeeded.")
            break
        except Exception as e:
            logging.info("DB connection failed. e: %s", e)
            logging.info("Traceback: ")
            logging.info(traceback.format_exc())
            logging.info("Waiting...")
            time.sleep(100)
            i = i + 1 
    logging.info("Exiting loop and returning result.")
    return db_connection_hardware
