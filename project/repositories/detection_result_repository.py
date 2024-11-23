from project.database import get_db

class DetectionResultRepository:
    def __init__(self, db):
        self.db = db

    def _serialize_document(self, document):
        # Convert ObjectId to string
        if '_id' in document:
            document['_id'] = str(document['_id'])
        return document
    
    def get_logs_by_request_path(self, request_path):
        logs = list(self.db.logs.find({"requestPath": request_path}))
        return logs

    def get_all_logs(self):
        # Convert the Cursor to a list of serialized documents
        logs = [self._serialize_document(doc) for doc in self.db.logs.find()]
        return logs
    
    def save(self, detection_result):
        result = self.db.detection_results.insert_one(detection_result)
        return result