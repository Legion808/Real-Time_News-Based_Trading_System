import requests

# Benzinga API URL va API kalitini to'g'ri qo'yish
url = "https://api.benzinga.com/api/v2/news"
api_key = "Your_API_key"  # o'zingizning API kalitingizni bu yerga qo'ying

# API parametrlarini sozlash
params = {
    "q": "stock market",  # Kalit so‘zlar
    "language": "en",
    "sortBy": "publishedAt",
    "apiKey": api_key
}

# API chaqiruvi
response = requests.get(url, params=params)

# Natijani tekshirish
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"API xatolik kodi: {response.status_code}")
    print(response.text)
