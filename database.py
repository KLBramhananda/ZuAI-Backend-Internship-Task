from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Update with your MongoDB URI
db = client['ia_ee_database']  # Database name
collection = db['ia_ee_collection']  # Collection name

# Function to insert or update data
def upsert_data(data):
    for record in data:
        collection.update_one(
            {"title": record["title"]},  # Unique identifier
            {"$set": record},  # Update or insert the record
            upsert=True
        )
    print("Data successfully upserted into MongoDB!")

# Function to fetch data
def fetch_data():
    return list(collection.find({}))

# Test connection
if __name__ == "__main__":
    print("Connected to MongoDB!")
