import requests
from datetime import datetime
import os

gen = "male"
wtkg = 90
htcm = 183
age = 23

ntrapid = os.environ["NT_APP_ID"]
ntrapky = os.environ["NT_API_KEY"]
ntrend = "https://trackapi.nutritionix.com/v2/natural/exercise"
shtend = os.environ["SHEET_ENDPOINT"]
uname = os.environ["USERNAME"]
pasd = os.environ["PASSWORD"]
# print(ntrapid, ntrapky, shtend)
txt = input("Tell which exercises you did?: ")

headers = {
    "x-app-id": ntrapid,
    "x-app-key": ntrapky
}

parm = {
    "query": txt,
    "gender": gen,
    "weight_kg": wtkg,
    "height_cm": htcm,
    "age": age
}

rsp = requests.post(url=ntrend, json=parm, headers=headers)
r1 = rsp.json()
print(r1)

tdy = datetime.now().strftime("%d%m%Y")
tm = datetime.now().strftime("%X")

for ex in r1["exercises"]:
    shtip = {
        "sheet1": {
            "date": tdy,
            "time": tm,
            "exercise": ex["name"].title(),
            "duration": ex["duration_min"],
            "calories": ex["nf_calories"]
        }
    }
    # print(shtip)
    rsp2 = requests.post(
        url=shtend,
        json=shtip,
        auth=(
            uname,
        pasd,
        )
    )
    # Basic Authentication

    # rsp2 = requests.post(url=shtend, json=shtip)
    # for No Authentication

    # bearer_headers = {
    #     "Authorization": "Bearer YOUR_TOKEN"
    # }
    # rsp2 = requests.post(url=shtend, json=shtip, headers=bearer_headers)
    # for Bearer Token Authentication
    print(rsp2.text)