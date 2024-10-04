import json
from datetime import datetime
import requests
import pandas as pd
import time

if __name__ == '__main__':
    # Target URL
    url = "https://newcastle.urbanobservatory.ac.uk/api/v1.1/sensors/PER_AIRMON_MONITOR1135100/data/json/?starttime=20230601&endtime=20230831"

    # Request data from Urban Observatory Platform
    resp = requests.get(url)

    # Convert response(Json) to dictionary format
    raw_data_dict = resp.json()

    data = raw_data_dict["sensors"][0]["data"]["PM2.5"]

    for index in data:
        timeStamp = index["Timestamp"]
        value = index["Value"]
        msg1 = f"Timestamp:{timeStamp} Value:{value}"
        msg1 = json.dumps(msg1)
    ##########################
    # outliers = []
    # for d in data:
    #     if d['Value'] >= 50:
    #         outliers.append(d)
    # print("outliers :", outliers)
    current_date = None
    daily_count = 0
    daily_total = 0
    daily_average = []
    for entry in data:
        timestamp = entry['Timestamp']
        value = entry['Value']
        date = datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d')
        if date != current_date:
            if current_date is not None:
                daily_average.append({'Date': current_date, 'Average_PM2.5': daily_total / daily_count})
                current_date = date
                daily_total = value
                daily_count = 1
            else:
                current_date = date

        else:
            daily_total += value
            daily_count += 1
    print("New format ", daily_average)

