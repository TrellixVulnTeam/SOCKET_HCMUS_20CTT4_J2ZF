# readme
# data 2021
# source https://vnexpress.net

import requests
import json
import time
import os
from datetime import datetime
class crawlDataCov:
    def __init__(self) -> None:
        #source data from 
        self.__url = "https://vnexpress.net/microservice/sheet/type/covid19_2021_281"
        self.__pathToDataCov = "./database/dataCov.json"
        self.__PlaceName = []
  
    def run(self):
        # print(self.crawlData())
        # self.writeToLocal(self.crawlData())
        __timeLoop = 60*60
        while True:
            self.writeToLocal(self.crawlData())
            time.sleep(__timeLoop)
  
    def crawlData(self):
        # load json => python
        # fetch data
        __rq = requests.get(self.__url)
        __data = __rq.text.split('\n')
        __headerName = __data[0].split(',')
        __headerName.pop(0)
        __headerName.pop()
        __headerName[1] = "TP. Hồ Chí Minh"

        # get place name dict
        for item in __headerName:
            self.__PlaceName.append(item.replace('\"',''))
        
        # build data
        __dataCov = {}
        __data.pop(0)
        __data.pop(0)
        __data.pop() 
        
        # a = __data[len(__data)-4].split(',')
        # a.pop(0)
        # print(int(a[1].replace('\"','')))
        for __dataOfDate in __data:
            __dataOf = __dataOfDate.split(',')
            __listDataAddress = {}
            __date = __dataOf[0].replace('\"','') + "/2021"
            __date = self.cleanTime(__date)
            __dataOf.pop(0)
            __dataOf.pop()
            # get data of 63 address
            for count in range(0,62):
                if __dataOf[count].replace('\"','') == '':
                    __listDataAddress[__headerName[count].replace('\"','')] = 0
                else:
                    __listDataAddress[__headerName[count].replace('\"','')] = int(__dataOf[count].replace('\"',''))
            __dataCov[__date] = __listDataAddress
        return __dataCov

    def cleanTime(self, dateStr):
        __format = "%d/%m/%Y"
        __dtObj = datetime.strptime(dateStr, __format) 
        return __dtObj.strftime(__format)

    def writeToLocal(self, data):
        if not os.path.exists(self.__pathToDataCov):
            __dataFileCov = open(self.__pathToDataCov, "x")
        else:
            __dataFileCov = open(self.__pathToDataCov, "w")
        json.dump(data, __dataFileCov, indent=3)
        __dataFileCov.close()

    def createAcronym(self, strg):
        if strg == "TP. Hồ Chí Minh":
            return "HCM"
        # add first letter
        oupt = strg[0]
        # iterate over string
        for i in range(1, len(strg)):
            if strg[i-1] == ' ':
                # add letter next to space
                oupt += strg[i]
        # uppercase oupt
        oupt = oupt.upper()
        return oupt

    def standardStr(self, strg):
        strg = strg.title()
        if strg.find("Tp") == 0:
            strg = strg.replace("Tp", "TP")
        return strg

    def query(self, city, time):
        city = self.standardStr(city)
        __dataFileCov = open(self.__pathToDataCov, "r")
        __data = json.load(__dataFileCov)
        result = []
        itemResult = {'resultAdrress': None, 'resultTodayCases': "NaN"}
        try:
            itemResult["resultAdrress"] = city
            itemResult["resultTodayCases"] = __data[time][city]
            result.append(itemResult)
            return result
        except:
            isFound = False
            city = city.upper()
            for item in self.__PlaceName:
                if city == self.createAcronym(item):
                    isFound = True
                    print(item)
                    itemResult["resultAdrress"] = item
                    try:
                        itemResult["resultTodayCases"] = __data[time][item]
                    except:
                        return [{'resultAdrress': None, 'resultTodayCases': "NaN"}]
                    result.append(itemResult)
                    itemResult = {'resultAdrress': None, 'resultTodayCases': "NaN"}
            if not isFound:
                result.append({'resultAdrress': None, 'resultTodayCases': "NaN"})
            return result
            

    
    

# def main():
#     cov = crawlDataCov()
#     # cov.run()
#     # str = "TP. Hồ Chí Minh"
#     # print(a)
#     cov.run()
#     a = cov.query("Quảng Ngãi", "15/12/2021")
#     print(a)

# if __name__ == "__main__":
#     main()