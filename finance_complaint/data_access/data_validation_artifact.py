from finance_complaint.config.mongo_client import MongodbClient
from finance_complaint.entity.artifact_entity import DataValidationArtifact


class DataValidationArtifactData:

    def __init__(self):
        self.client = MongodbClient()
        self.collection_name = "data_validation_artifact"
        self.collection = self.client.database[self.collection_name]
    ##Below are all the CRUD operations
    def save_artifact(self, artifact: DataValidationArtifact):
        self.collection.insert_one(artifact._asdict())  #to covert named tuple into dict()

    def get_artifact(self, query):
        self.collection.find_one(query)

    def update_artifact(self, query, artifact: DataValidationArtifact):
        self.collection.update_one(query, artifact._asdict())

    def remove_artifact(self, query):
        self.collection.delete_one(query)

    def remove_artifacts(self, query):
        self.collection.delete_many(query)

    def get_artifacts(self, query):
        self.collection.find(query)
