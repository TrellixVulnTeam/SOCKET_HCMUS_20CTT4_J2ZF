import os
import json
from bstTree import *

class user(object):
    def __init__(self, username, password):
        self.__usr = {
            "username": username,
            "password": password
        }
    def valueOf(self):
        return self.__usr

class userDB(object):
    def __init__(self):
        self.__pathToDB = "./database/userDB.json"

    def writeToLocal(self, usr):
        self.__user = usr.valueOf()
        if(os.path.exists(self.__pathToDB)):
            self.__dataFileUSR = open(self.__pathToDB, "a")
            self.__dataFileUSR.seek(self.__dataFileUSR.tell() - 3, os.SEEK_SET)
            self.__dataFileUSR.truncate()
            self.__dataFileUSR.write(",\n\t")
        else:
            self.__dataFileUSR = open(self.__pathToDB, "x")
            self.__dataFileUSR.write("[\n\t")
        json.dump(self.__user,self.__dataFileUSR)
        self.__dataFileUSR.write("\n]")  
        self.__dataFileUSR.close()

    def updateLocal(self):
        pass
    def query(self, name):
        self.__dataFileUSR = open(self.__pathToDB,)
        __USR = json.load(self.__dataFileUSR)
        self.__dataFileUSR.close()
        __rootUSR = None
        __USRAVLtree = AVLtree()
        __keyName = "username"
        for __dataOfUSR in __USR:
            __rootUSR = __USRAVLtree.insert(__rootUSR, __dataOfUSR, __keyName)
        __result = __USRAVLtree.search(__rootUSR, name, __keyName)
        return __result.val

def main():
    username = "c"
    password = "1"
    a = user(username,password)
    db = userDB()
    db.writeToLocal(a)

    # print(db.query("b"))
    print(db.query(username))
main()