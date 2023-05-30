import logging
import logging.config
from config import read_configuration
from connection import MySQL, establish_db_connection # pipenv install mysqlclient
import query
import pandas as pd # pipenv install pandas
import openpyxl # pipenv install openpyxl
import os
import time



def main(config):
    logging.config.fileConfig(config.APP.LOGGING_CONFIG)
    logging.info("Database manager starting.")

    db_mov = establish_db_connection(config=config)

    query_type = db_mov.execute(query.type_get_name)
    logging.info(query_type)  # [['drama'], ['comedy'], ['documentary']]


    # save list locally as excel
    df = pd.DataFrame(query_type)

    excel_file_name = "excel_test.xlsx"
    excel_file_path = os.getcwd() + "/" + excel_file_name

    #excel_file_path = config.APP.SAVE_FOLDER + "excel_test.xlsx"
    #excel_file_path = "excel_test.xlsx"
    logging.info("excel_file_path: %s", excel_file_path)   # /usr/app/src/excel_test.xlsx
    df.to_excel(excel_writer=excel_file_path, sheet_name="1")  # ADDED excel writer
    logging.info("Excel saved")

    logging.info("Waiting...")
    time.sleep(1200)


# This will only be executed if main.py is run directly, but not when it is imported as a module. If you import main.py into another script, the code inside the if block will not be executed, but you can still access the functions defined in main.py for reuse in other modules.
if __name__ == "__main__":
    configuration = read_configuration()
    main(configuration)

