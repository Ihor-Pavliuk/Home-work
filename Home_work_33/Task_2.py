#Load data

#Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ . 

#As a result, store all comments in chronological order in JSON and dump it to a file.

import requests
import json
import datetime

def fetch_apod(api_key, date):
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}"
    response = requests.get(url)
    return response.json()

def load_apods(api_key, start_date, end_date):
    apods = []
    current_date = start_date
    while current_date <= end_date:
        apod = fetch_apod(api_key, current_date)
        apods.append(apod)
        current_date += datetime.timedelta(days=1)
    return apods

if __name__ == "__main__":
    api_key = "DEMO_KEY" 
    start_date = datetime.date(2022, 12, 1)
    end_date = datetime.date(2022, 12, 31)
    
    apods = load_apods(api_key, start_date, end_date)

    with open('apods.json', 'w') as f:
        json.dump(apods, f, indent=4, ensure_ascii=False)



