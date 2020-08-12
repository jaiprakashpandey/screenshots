
#from configs import ScreenDatabaseConfig
#from database import ScreenDatabaseConnection
from configs import ScreenConfigurations
import pymongo
from pymongo import MongoClient

#db_config = ScreenDatabaseConfig()
db_config = ScreenConfigurations()

# fails for multi processing - should be rechecked
#db_conn = ScreenDatabaseConnection()


def mp_persist(screen_shot):
	# db_conn has some config issues-TO-do , parking as time constraint 
	#mongo_client = db_conn._get_screen_shots_db_con()	
	client = MongoClient(db_config.mongo_db_url)
	screen_db = client.test
	screen_collection = pymongo.collection.Collection(screen_db, db_config.screens_shots_collections)
	
	_ids = screen_collection.insert_one(screen_shot)
	return _ids