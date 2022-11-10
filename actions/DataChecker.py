from database import Database
import bcrypt

class DataChecker():

    def __init__(self, collection):
        self.collection = collection
        self.db = Database.Database().db
        

    def check_name(self, name):

        data = self.db.get_collection(self.collection).find_one({"username": name})
        if(data is not None):
            return True
        else:
            return False

    def check_password(self, username, password):

        data = self.db.get_collection(self.collection).find_one({"username": username})

        if(data is not None):
            passDB = data["password"]
            password = password.encode("UTF-8")
            result = bcrypt.checkpw(password, passDB.encode("UTF-8"))
            if(result == True):
                return True
        else:
            return False