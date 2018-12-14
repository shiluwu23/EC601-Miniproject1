import pymongo
import datetime
from time import time,localtime,asctime

def clear_base():
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.ec601mini3
    collection = db.mini3_database
    collection.drop()


def mongoDb(twnum,picnum,picaddress,newtag):
        #Connect to mongoDB
        client = pymongo.MongoClient(host='localhost', port=27017)

        # Specify a database.
        db = client.ec601mini3

        # Specify a collection.
        #
        collection = db.mini3_database
        # INsert information into collection.
        mini3_database = {"time":asctime(localtime(time())),"twtnum":twnum,"picnum":picnum,"picaddress":picaddress,"tags":newtag}
        times = datetime.datetime.now()
        #print(times)

        result = collection.insert(mini3_database)
        #print(type(result))
        #print(result)

        results = collection.find({'tags': newtag})
        result = []
        for user in results:
            result.append(user['tags'])
        
        return result

def search_keyword(keyword):
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
    c = collection.find()
    dic={}
    for i in c:
    	if i['tags'] in dic:
    		dic[i['tags']] +=1
    	else:
    		dic[i['tags']] =1
    ans = max(dic.items(), key=lambda x: x[1])
    return ans


if __name__ == '__main__':
    clear_base()
    mongoDb("1","picnum1","picaddressA","newtag")
    mongoDb("2","picnum2","picaddressB","newtag2")
    mongoDb("3","picnum3","picaddressC","newtag2")
    mongoDb("4","picnum4","picaddressD","newtag2")
    mongoDb("5","picnum5","picaddressE","newtag3")
    mongoDb("6","picnum6","picaddressF","newtag3")
    mongoDb("7","picnum7","picaddressG","newtag4")
    search_keyword('newtag')
    print(most_popular())
