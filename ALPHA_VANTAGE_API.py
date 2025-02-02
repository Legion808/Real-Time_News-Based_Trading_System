import requests

# Alpha Vantage API kaliti
ALPHA_VANTAGE_API_KEY = "5W3TM9B33FLNODZ1"

# API URL
ALPHA_VANTAGE_URL = "https://www.alphavantage.co/query"

# API parametrlarini belgilash
params = {
    "function": "NEWS_SENTIMENT",
    "apikey": ALPHA_VANTAGE_API_KEY
}

# API chaqirish
response = requests.get(ALPHA_VANTAGE_URL, params=params)

# JSON formatidagi javobni olish
news_data1 = response.json()

# Natijani ekranga chiqarish
print(news_data1)
