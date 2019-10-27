from app import mongo


class Medication:
    rel_path = 'medications'

    @classmethod
    def save(self, data):
        doc = mongo.db[self.rel_path].find_one(data)
        if doc:
            return mongo.db[self.rel_path].update_one(doc, {'$set': data})
        return mongo.db[self.rel_path].insert_one(data)
