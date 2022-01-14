import requests
from datetime import datetime

gen = "male"
wtkg = 90
htcm = 183
age = 23

ntrapid = "3b00ae3f"
ntrapky = "6e4bd88489aef0199b2f31af674d9285"
ntrend = "https://trackapi.nutritionix.com/v2/natural/exercise"
shtend = "https://api.sheety.co/cc1a85acef0ef2251d6e2213f6f14c66/myWorkouts/sheet1"

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
# print(r1)

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
            "aravindvas",
        "mailme1997",
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