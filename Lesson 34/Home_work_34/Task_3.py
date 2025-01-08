import threading
import requests
import json

def fetch_apod(url):
    response = requests.get(url)
    return response.json()

def thread_worker(url, results, index):
    results[index] = fetch_apod(url)

def multithreading_requests(urls):
    threads = []
    results = [None] * len(urls)
    
    for i, url in enumerate(urls):
        thread = threading.Thread(target=thread_worker, args=(url, results, i))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    return results

if __name__ == "__main__":
    api_key = "DEMO_KEY" 
    api_url = "https://api.nasa.gov/planetary/apod"
    urls = [f"{api_url}?api_key={api_key}&date=2022-12-{i:02d}" for i in range(1, 31)]
    
    results = multithreading_requests(urls)

    sorted_results = sorted(results, key=lambda x: x['date'])

    with open('apod_multithreading.json', 'w') as f:
        json.dump(sorted_results, f, indent=4, ensure_ascii=False)


