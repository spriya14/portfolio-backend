import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

# Make sure this is the correct absolute or relative path
load_dotenv(dotenv_path="/home/spbatson/pet_projects/ARTSY/my-website-backend/secrets.env")

# Now try to get the value
mongo_uri = os.getenv("MONGO_URI")
uri = mongo_uri

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)