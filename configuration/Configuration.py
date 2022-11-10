import json

class Configuration():
    
    jsonFile = open("config.json")
    data = json.load(jsonFile)

    url = data["database_url"]
    dbname = data["database_name"]
    colltag = data["collection_tag"]
    