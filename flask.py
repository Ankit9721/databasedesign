import pymongo
if __name__ == '__main__':
    Client =pymongo.MongoClient("mongodb+srv://ankitmaurya899:Suresh%409721@cluster1.3b5vdsa.mongodb.net/")
    db = Client["wishom collection"]
    collection = db.class1
    studentInfo = {
        "name": "harry",
        "section":1,
        "maths_makrs":100,
    }
    student_id = collection.insert_one(studentInfo).inserted_id
    print(f"student with id {student_id} has been craeted")
