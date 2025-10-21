# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username
        PASS = password
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            try:
                self.database.animals.insert_one(data)  # data should be dictionary   
                return True # return true if successful
            except Exception as e:
                print('An error occured while trying to insert the record: ' + str(e))
                return False # return false if unsuccessful
        else: 
            raise Exception("Nothing to save, because data parameter is empty")
            return False
        

    # Create method to implement the R in CRUD.
    def read(self, data):
        result = []
        if data is not None:
            try:
                result = list(self.collection.find(data))
                return result # return a 
            except Exception as e:
                print('An error occured while trying to query for the record: ' + str(e))
                result = [] # ensure result is empty before returning on an error
                return result
        else:
            raise Exception("Nothing was passed in to query")
            
            
    # Create method to implement the U in CRUD.
    def update(self, data, updateOperation):
        if data is not None and updateOperation is not None: # Only run if both parameters are valid
            try:
                result = self.database.animals.update_many(data, updateOperation)
                return str(result.modified_count) + " records have been updated."
            except Exception as e:
                print('An error occured while trying to query or updating the record: ' + str(e))
                return "Nothing returned"
        return
    
    # Create method to implement the D in CRUD.
    def delete(self, data):
        if data is not None:
            try:
                result = self.database.animals.delete_many(data) # This will delete any records that match
                return str(result.deleted_count) + " records were deleted."
            except Exception as e:
                print('An error occured while trying to query for the record: ' + str(e))
                return "Nothing returned"
        else:
            raise Exception("Nothing was passed in to query and delete records")