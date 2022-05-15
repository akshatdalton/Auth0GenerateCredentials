import pymongo
import datetime

################# USER INPUT #################

MONGO_URI = ""
DB_NAME = "markov"
COLLECTION_NAME = "token"

##############################################


client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]
token_collection = db[COLLECTION_NAME]

CREATED_AT_INDEX = "createdAt"

if f"{CREATED_AT_INDEX}_1" not in token_collection.index_information():
    # we create an index one time only to not raise any error.
    token_collection.create_index(CREATED_AT_INDEX, expireAfterSeconds=15)

def insert_access_token(access_token, expireAfterSeconds):
    # Update `expireAfterSeconds` for the new `access_token`.
    result = db.command("collMod", COLLECTION_NAME, index={"keyPattern": {CREATED_AT_INDEX: 1}, "expireAfterSeconds": expireAfterSeconds})
    if result["ok"] != 1.0:
        print("Some error occured during insertion")
        return

    current_date = datetime.datetime.utcnow()
    post = {"access_token": access_token, CREATED_AT_INDEX: current_date}
    token_collection.insert_one(post)


def get_access_token():
    doc = token_collection.find_one()
    if doc is not None:
        return doc["access_token"]
    return None
