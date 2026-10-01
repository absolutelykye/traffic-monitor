import requests,time,json
import pandas as pd 
import datetime as dt



url='https://routes.googleapis.com/directions/v2:computeRoutes'

with open("request.json","r") as f:
    data=json.load(f)
with open("headers.json", "r") as f :
    headers=json.load(f)


#checking if csv file already exists, if not it will create a new one

try :
    route_table = pd.read_csv("routes.csv")
except FileNotFoundError : 
    route_table = pd.DataFrame(
        {
            "day":[],
            "month":[],
            "time":[],
            "distance":[],
            "duration":[],
            "staticDur":[]
        }
    )

#temp variables for later use
temp=dict()
timedate=""

def routes_info():
    try :
        route = requests.post(url=url, json=data, headers=headers)
        print(f"request sent, status code : {route.status_code} ")
        route.raise_for_status()
        route_json = route.json()
        timedate = dt.datetime.now()
        temp = {
                    "day":timedate.strftime("%d"),
                    "month":timedate.strftime("%B"),
                    "time":timedate.strftime("%I:%M:%S"),
                    "distance":route_json["routes"][0]["distanceMeters"],
                    "duration":route_json["routes"][0]["duration"],
                    "staticDur":route_json["routes"][0]["staticDuration"]
                }
        # appending the entry to the dataframe
        route_table.loc[len(route_table)]=temp
        #writing to the csv file
        route_table.to_csv("routes.csv", index=False)
    except requests.exceptions.RequestException as err :
        print(f"error : {err}")

#function calling loop 
if __name__ == "__main__":
    while True :
        routes_info()
        time.sleep(3600)

    



