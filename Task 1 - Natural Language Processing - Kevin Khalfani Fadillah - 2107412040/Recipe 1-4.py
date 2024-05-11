import requests
import json

#json from "https://quotes.rest/qod.json"
response = requests.get("https://dummyjson.com/quotes/1")

res = response.json()
print(json.dumps(res, indent = 4))

quote = res['quote']
author = res['author']

print(f"Quote: {quote}\nAuthor: {author}")