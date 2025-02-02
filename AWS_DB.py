import boto3
from NewsAPI_NLP import news_data
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("NewsSentiment")

for article in news_data["articles"]:
    table.put_item(
        Item={
            "title": article["title"],
            "description": article["description"],
            "publishedAt": article["publishedAt"],
            "source": article["source"]["name"]
        }
    )

print("Ma'lumotlar AWS DynamoDB ga yuklandi!")
