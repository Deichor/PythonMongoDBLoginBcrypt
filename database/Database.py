from pymongo import MongoClient

class Database():
    
    def connect(self, url, databaseName):

        client = MongoClient(url)
        Database.db = client[databaseName]
        
        return Database.db

    def create_collection(self, db, colltag):
        
        collname = colltag + "users"

        if (collname not in db.list_collection_names()):
            db.create_collection(collname)
        
            
