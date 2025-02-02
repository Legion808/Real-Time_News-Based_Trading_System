import json

from NewsAPI_NLP import news_data
from ALPHA_VANTAGE_API import news_data1
from BENZINGA_API import data

# JSON ma'lumotlarini faylga saqlash
with open("alpha_vantage_news.json", "w") as file:
    json.dump(news_data1, file, indent=4)

# JSON ma'lumotlarini faylga saqlash
with open("news_data.json", "w") as file:
    json.dump(news_data, file, indent=4)

# JSON ma'lumotlarini faylga saqlash
with open("Benzinga_data.json", "w") as file:
    json.dump(data, file, indent=4)



print("Ma'lumotlar muvaffaqiyatli saqlandi!")
