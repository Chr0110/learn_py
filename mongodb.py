import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27/')

print(myclient.list_database_names())
