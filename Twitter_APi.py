import requests
import json
BEARER_TOKEN = "Your_API"


def fetch_tweets(query, max_results=100):
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    url = f"https://api.twitter.com/2/tweets/search/recent"
    params = {
        "query": query,
        "max_results": max_results,
        "tweet.fields": "created_at,text,author_id,public_metrics",
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None


# Fetch tweets related to Apple stock
tweets = fetch_tweets("AAPL stock news")
print(tweets)

# JSON ma'lumotlarini faylga saqlash
with open("Twitter_data.json", "w") as file:
    json.dump(tweets, file, indent=4)
