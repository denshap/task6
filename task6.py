import json
import requests
res= requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
d=json.loads(res.text)
for i in d:
    print(i["base_ccy"],'/', i["ccy"], ':', i["buy"],'/', i["sale"])
