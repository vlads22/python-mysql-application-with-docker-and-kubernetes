import logging
import logging.config
from config import read_configuration
from connection import MySQL
import query

# i have a python script the make a query to a mysql database and returns the result and the database saved as a sql file. i want to have two containers, one for the python script and the other for the mysql db. how do i make the containers then write a docker compose file that uses the two containers?

def main(config):
    logging.config.fileConfig(config.APP.LOGGING_CONFIG)

    db_connection_hardware = MySQL(host=config.DB_HARDWARE.HOST, port=config.DB_HARDWARE.PORT,
                                   user=config.DB_HARDWARE.USER, passwd=config.DB_HARDWARE.PASSWORD, database=config.DB_HARDWARE.DATABASE)

    query_type = db_connection_hardware.execute(query.type_get_name)
    logging.info(query_type)


if __name__ == "__main__":
    configuration = read_configuration()
    main(configuration)
