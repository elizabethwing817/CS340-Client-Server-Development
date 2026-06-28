from pymongo import MongoClient
from pymongo.errors import PyMongoError


class AnimalShelter:
    """CRUD operations for the AAC animal shelter database."""

    def __init__(self, username, password):
        """Initialize MongoDB connection."""
        self.client = MongoClient(
            "mongodb://%s:%s@localhost:27017" % (username, password)
        )
        self.database = self.client["aac"]
        self.collection = self.database["animals"]

    def create(self, data):
        """Insert a document into the animals collection."""
        if data is not None and isinstance(data, dict):
            try:
                result = self.collection.insert_one(data)
                return result.acknowledged
            except PyMongoError as error:
                print("Create error:", error)
                return False
        return False

    def read(self, query):
        """Query documents from the animals collection."""
        if query is not None and isinstance(query, dict):
            try:
                results = list(self.collection.find(query))
                return results
            except PyMongoError as error:
                print("Read error:", error)
                return []
        return []

    def update(self, query, new_values):
        """Update document(s) in the animals collection."""
        if query is not None and isinstance(query, dict):
            if new_values is not None and isinstance(new_values, dict):
                try:
                    result = self.collection.update_many(
                        query,
                        {"$set": new_values}
                    )
                    return result.modified_count
                except PyMongoError as error:
                    print("Update error:", error)
                    return 0
        return 0

    def delete(self, query):
        """Delete document(s) from the animals collection."""
        if query is not None and isinstance(query, dict):
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except PyMongoError as error:
                print("Delete error:", error)
                return 0
        return 0