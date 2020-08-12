from configs import ScreenConfigurations
import sys
from pymongo import MongoClient

db_config = ScreenConfigurations()

class ScreenDatabaseConnection:
    def __init__(self):
        print(' db constructor')

    def _get_screen_shots_db_con(self):        
        try:            
            client = MongoClient(db_config.mongo_db_url)
            log.info('Connection Sucecssful')            
        except:
            print("Could not connect to MongoDB" + str(sys.exc_info()[0]))
        else:
            return client