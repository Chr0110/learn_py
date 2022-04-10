import pymongo
import certifi
ca = certifi.where()

myclient = pymongo.MongoClient(f"mongodb+srv://Fristcluster:ZadeQm_kwwsZuJ2@cluster0.3zolr.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)


print(myclient.list_database_names())
mydb = myclient["test"]
mycol = mydb["students"]
mydict = {
    "last name": "eradi",
    "first name": "el mehdi",
    "campus": "benguerir"
}
x = mycol.insert_one(mydict)