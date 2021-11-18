import requests
import json
# source data from https://ncov.moh.gov.vn/
url = "https://static.pipezero.com/covid/data.json"
rq = requests.get(url)
# json => python
dataCov = json.loads(rq.text)
# obj database to save them
for dataCovProvince in dataCov["locations"]:
  print(dataCovProvince["name"])
