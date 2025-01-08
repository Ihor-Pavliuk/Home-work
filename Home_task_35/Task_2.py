

import multiprocessing
import requests
import json

def fetch_comments(url):
    response = requests.get(url)
    return response.json()

def process_worker(url, results, index):
    results[index] = fetch_comments(url)

def multiprocessing_requests(urls):
    processes = []
    manager = multiprocessing.Manager()
    results = manager.list([None] * len(urls))
    
    for i, url in enumerate(urls):
        process = multiprocessing.Process(target=process_worker, args=(url, results, i)) 
        processes.append(process) 
        process.start()

    for process in processes: 
        process.join() 
        
    return list(results)

if __name__ == "__main__":
    api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    urls = [f"{api_url}&date=2022-12-{i:02d}" for i in range(1, 31)]
    
    process_results = multiprocessing_requests(urls)

    with open('apod_multiprocessing.json', 'w') as f:
        json.dump(process_results, f, indent=4, ensure_ascii=False)
    

