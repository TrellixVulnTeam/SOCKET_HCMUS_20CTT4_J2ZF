import os
import json

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
        if(os.path.exists(self.__pathToDB)):
            self.__dataFileUSR = open(self.__pathToDB)
            self.__user = json.load(self.__dataFileUSR)
            self.__dataFileUSR.close()
            self.__user[usr.valueOf()["username"]] = usr.valueOf()
            self.__dataFileUSR = open(self.__pathToDB, "w")
        else:
            self.__dataFileUSR = open(self.__pathToDB, "x")
            self.__user = {usr.valueOf()["username"] : usr.valueOf()}
        json.dump(self.__user,self.__dataFileUSR, indent=2)
        self.__dataFileUSR.close()

    def checkID(self, username):
        self.__dataFileUSR = open(self.__pathToDB)
        __USR = json.load(self.__dataFileUSR)
        self.__dataFileUSR.close()
        __keyName = username
        try:
            if __USR[__keyName]:
                return True
        except:
            return False
            
    def checkPass(self, username, password):
        self.__dataFileUSR = open(self.__pathToDB)
        __USR = json.load(self.__dataFileUSR)
        self.__dataFileUSR.close()
        __keyName = username
        try:
            usrItem = __USR[__keyName]
            if usrItem["password"] == password:
                return True
            else:
                return False
        except:
            return False
