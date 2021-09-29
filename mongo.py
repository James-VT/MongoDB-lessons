import os
import pymongo
# The below is how we link to our credentials in the env.py file. It exists as
# an if check to see if the file even exists. If not, nothing works.
if os.path.exists("env.py"):
    import env

# Python constants - might also be called environment variables? - are written
# in caps as a rule
MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDBJT"
COLLECTION = "celebritiesJT"


# This function connects to the database
def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


# Here's where we call the function - MONGO_URI is going in as the URL
# argument, since that carries the URL for the database
conn = mongo_connect(MONGO_URI)
# Here is the connection object with our database - note the use of the
# constant variables declared above
coll = conn[DATABASE][COLLECTION]

# The below two lines are for adding new records to the database. Simply write
# the records as "key":"value" pairs
# bearing in mind that in PyMongo you must wrap keys in quotations as well as
# their values.
# Records must be written as a dictionary.
# Put these records in a variable, then feed the variable into the method as
# an argument.
# For the insert_many, write your record as an array of dictionaries.

# coll.insert()
# coll.insert_many()

# The below code updates only the first entry with the nationality of American.
# To update all with the nationality of American, use .update_all()
coll.update_one({"nationality": "american"},
                {"$set": {"hair_color": "maroon"}})
# The MongoDB code there for coll.find() finds all items from the collection
# and shoves them into the documents variable
# This returns a "cursor", which is a MongoDB object kind of like a dictionary,
# and needs to be iterated over


documents = coll.find({"nationality": "american"})

for doc in documents:
    print(doc)
