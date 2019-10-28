from app import mongo


class Medication:
    rel_path = 'medications'

    @classmethod
    def save(cls, data):
        doc = mongo.db[cls.rel_path].find_one(data)
        if doc:
            return mongo.db[cls.rel_path].update_one(doc, {'$set': data})
        return mongo.db[cls.rel_path].insert_one(data)

    @classmethod
    def all(cls):
        return mongo.db[cls.rel_path].find({})
