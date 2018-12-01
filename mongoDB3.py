import pymongo
import datetime
from time import time,localtime,asctime



def mongoDb(twnum,picnum,picaddress,newtag):
        #Connect to mongoDB
        client = pymongo.MongoClient(host='localhost', port=27017)
        # Specify a database.
        db = client.ec601mini3
        # Specify a collection.
        collection = db.mini3_database
        # INsert information into collection.
        mini3_database = {"time":asctime(localtime(time())),"twtnum":twnum,"picnum":picnum,"picaddress":picaddress,"tags":newtag}
        times = datetime.datetime.now()
        print(times)

        result = collection.insert(mini3_database)
        print(type(result))
        print(result)

        results = collection.find({'tags': newtag})
        result = []
        for user in results:
            result.append(user['tags'])

        return result
        print(result)

def search_keyword(keyword):
        word = input("Enter a word to search: ")
        client = pymongo.MongoClient(host='localhost', port=27017)
        db = client.ec601mini3
        collection = db.mini3_database
        for info in collection.find({"$or":[{"tags":keyword},{"picaddress":keyword}]}):
            print(info)


def num_perfeed():
    myclient = pymongo.MongoClient(host='localhost', port=27017)
    mydb = myclient["ec601mini3"]
    mycol = mydb["users"]
    x = mycol.aggregate([{"$group":{"_id":"average","value":{"$avg":"$Pictures"}}}])
    print(list(x)[0])


def most_popular():
    client = pymongo.MongoClient(host='localhost', port=27017)
# Specify a database.
    db = client.ec601mini3
# Specify a collection.
    collection = db.mini3_database
    c = collection.aggregate([{"$group":{"_id":"$Descriptor","Frequency":{"$sum":1}}}])
    print(list(c)[0])

if __name__ == '__main__':
    mongoDb("twnum","picnum","picaddress","newtag")
    search_keyword('keyword')
    num_perfeed()
    most_popular()
