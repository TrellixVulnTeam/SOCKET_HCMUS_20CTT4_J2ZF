import requests
import json
import time
import os
from bstTree import *
class crawlDataCov:
  def __init__(self) -> None:
    # source data from https://ncov.moh.gov.vn/
    self.__url = "https://static.pipezero.com/covid/data.json"
    self.__pathToDataCov = "./database/dataCov.json"
  
  def run(self):
    # __timeLoop = 1h = 60phut = 60 * 60 s
    __timeLoop = 60*60 
    __startTime = time.time()
    while True:
      __currentTime = time.time()
      __elapsedTime = __currentTime - __startTime
      if __elapsedTime == __timeLoop or __elapsedTime == 0:
        self.__dataCov = self.crawlData()
        self.writeToLocal()
  
  def crawlData(self):
    # load json => python
    __rq = requests.get(self.__url)
    __dataCov = json.loads(__rq.text)
    return __dataCov["locations"]

  def writeToLocal(self):
    if(os.path.exists(self.__pathToDataCov)):
      self.__dataFileCov = open(self.__pathToDataCov, "w")
    else:
      self.__dataFileCov = open(self.__pathToDataCov, "x")
    self.__dataFileCov.write("[\n")
    for __dataCovProvince in self.__dataCov:
      self.__dataFileCov.write("\t")
      json.dump(__dataCovProvince,self.__dataFileCov)
      self.__dataFileCov.write(",\n")
    self.__dataFileCov.seek(self.__dataFileCov.tell() - 3, os.SEEK_SET)
    self.__dataFileCov.truncate()
    self.__dataFileCov.write("\n]")
    self.__dataFileCov.close()

  def query(self, name):
    self.__dataFileCov = open(self.__pathToDataCov,)
    __dataCov = json.load(self.__dataFileCov)
    self.__dataFileCov.close()
    __rootCov = None
    __covAVLtree = AVLtree()
    __keyName = "name"
    for __dataCovProvince in __dataCov:
      __rootCov = __covAVLtree.insert(__rootCov, __dataCovProvince, __keyName)
    __result = __covAVLtree.search(__rootCov, name, __keyName)
    return __result.val

def main():
    cov = crawlDataCov()
    # cov.run()
    print(cov.query("TP. Hồ Chí Minh"))

if __name__ == "__main__":
    main()
