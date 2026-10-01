# Traffic Monitor

A traffic monitor program written in python which periodically fetches data from Google Routes API  and calculates time required to travel from one point to another. Collected observations are stored in a CSV file and can be used to with data analysis libraries like pandas and matplotlib to analyse the varying traffic trends throughout the day.

Program Workflow : 
1. Sends a POST request to Google Routes API 
2. Receives the static travel time(ignoring traffic conditions), actual travel time, distance.
3. Records the observation timestamp and stores them in a dataframe.
4. Then it stores the dataframe onto a CSV file.
5. This process is repeated in a given interval (default setting is per hour)

### Collecting Data
`request.json` file contains the data you need to provide to Routes API to get back valid readings.

Example : 
```JSON
{ "origin": { "address": "Origin" }, "destination": { "address": "Destination" }, "travelMode": "DRIVE", "routingPreference": "TRAFFIC_AWARE" }
```
### Installation 
Clone the repo :
```bash
git clone https://github.com/absolutelykye/traffic-monitor
cd traffic-monitor 
```
Create a python virtual environment :
```bash
python3 -m venv .venv
source .venv/bin/activate
```
Install Dependancies :
```bash
pip install -r requirements.txt
```

#### API key 
Put your api key in the `headers.json` file in the `"X-Goog-Api-Key" : "your key"` field.

### Sample Data
I have also put a CSV file of sample data (`sample_data.csv`) with smaller intervals and a handful of readings, you can use those inside of `analysis.py` to plot graphs with sample data.


## Running the program

`python3 data_fetcher.py`
or
`python data_fetcher.py`
