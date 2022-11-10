from actions import Return
from configuration import Configuration
from database import Database

class Main():

    #configuration
    cfg = Configuration.Configuration()

    #database
    db = Database.Database().connect(cfg.url, cfg.dbname)
    Database.Database().create_collection(db, cfg.colltag)


    Return.Returner().get_input()
