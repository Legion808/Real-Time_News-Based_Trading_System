import requests
import json

NEWS_API_KEY = "ca4c112b25d84ed0af84cb31a8e38497"
NEWS_API_URL = "https://newsapi.org/v2/everything"

params = {
    "q": "stock market",  # Kalit so‘zlar
    "language": "en",
    "sortBy": "publishedAt",
    "apiKey": NEWS_API_KEY
}

response = requests.get(NEWS_API_URL, params=params)
news_data = response.json()  # JSON formatidagi javobni olish

# Natijani ekranga chiqarish
print(news_data)


# JSON ma'lumotlarini faylga saqlash
with open("news_data.json", "w") as file:
    json.dump(news_data, file, indent=4)