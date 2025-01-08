import requests

response = requests.get("https://en.wikipedia.org/robots.txt")
with open("robots.txt", "w") as file:
    content = file.write(str(response.content))

    
