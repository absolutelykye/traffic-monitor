import requests,time,csv,json,os
import pandas as pd 
import datetime as dt



url='https://routes.googleapis.com/directions/v2:computeRoutes'

with open("request.json","r") as f:
    data=json.load(f)
with open("headers.json", "r") as f :
    headers=json.load(f)

try :
    route_table=pd.read_csv("routes.csv")
except FileNotFoundError : 
    route_table=pd.DataFrame(
        {
            "day":[],
            "month":[],
            "time":[],
            "distance":[],
            "duration":[],
            "staticDur":[]
        }
    )


temp=dict()
timedate=""

def routes_info():
    try :
        route = requests.post(url=url, json=data, headers=headers)
        print(f"Request sent, status code : {route.status_code} ")
        route.raise_for_status()
        route_json=route.json()
        timedate=dt.datetime.now()
        temp = {
                    "day":timedate.strftime("%d"),
                    "month":timedate.strftime("%B"),
                    "time":timedate.time(),
                    "distance":route_json["routes"][0]["distanceMeters"],
                    "duration":route_json["routes"][0]["duration"],
                    "staticDur":route_json["routes"][0]["staticDuration"]
                }
        route_table.loc[len(route_table)]=temp
        route_table.to_csv("routes.csv", index=False)
    except requests.exceptions.RequestException as err :
        print(f"error : {err}")


if __name__ == "__main__":
    while True :
        routes_info()
        time.sleep(5)

    



