import asyncio
import requests # реквест тут не доцільно використовувати, оскільки він не підтримує асинхрон. Але це прстіше, ніж лізти і розбиратися з httpx чи aiohttp 
import json

async def fetch(url):
    response = requests.get(url)
    return response.json()

async def fetch_apods():
    api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    apods = []
    for i in range(1, 31):
        url = f"{api_url}&date=2022-12-{i:02d}"
        apod = await fetch(url)
        apods.append(apod)
    return apods

async def main():
    apods = await fetch_apods()
    with open('apods.json', 'w') as f:
        json.dump(apods, f, indent=4, ensure_ascii=False)

asyncio.run(main())
