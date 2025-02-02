import json
import boto3
from transformers import pipeline
from huggingface_hub import HfApi

# Hugging Face loginni sozlash
HfApi().set_access_token("your_huggingface_token_here")  # O'zingizning API tokeningizni kiriting

# AWS Comprehend va FinBERT sozlamalari
comprehend = boto3.client(
    'comprehend',
    aws_access_key_id='your_access_key',  # To'g'ri kredentiallarni kiriting
    aws_secret_access_key='your_secret_key',
    region_name='us-east-1'
)
finbert = pipeline('sentiment-analysis', model='yiyanghkust/finbert-financial')


# Yangiliklar sentiment tahlili
def analyze_sentiment(text):
    try:
        response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
        sentiment = response['Sentiment']
        if sentiment == 'POSITIVE':
            return {'sentiment': 'bullish', 'sentiment_score': 1}
        elif sentiment == 'NEGATIVE':
            return {'sentiment': 'bearish', 'sentiment_score': -1}
        else:
            return {'sentiment': 'neutral', 'sentiment_score': 0}
    except Exception as e:
        print(f"AWS Error: {str(e)}")
        try:
            result = finbert(text)[0]
            sentiment = result['label']
            return {
                'sentiment': 'bullish' if sentiment == 'positive' else 'bearish' if sentiment == 'negative' else 'neutral',
                'sentiment_score': result['score']
            }
        except Exception as ferr:
            print(f"FinBERT Error: {str(ferr)}")
            return {'sentiment': 'neutral', 'sentiment_score': 0}


# Kalit so‘zlarni chiqarish
def extract_keywords(text):
    response = comprehend.detect_key_phrases(
        Text=text,
        LanguageCode='en'
    )
    return [phrase['Text'] for phrase in response['KeyPhrases']]


# DynamoDB davlatlarni saqlash
def save_to_dynamodb(news_id, sentiment_analysis, keywords):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('MarketSentiment')
    table.put_item(
        Item={
            'news_id': news_id,
            'sentiment': sentiment_analysis['sentiment'],
            'score': sentiment_analysis['sentiment_score'],
            'keywords': keywords
        }
    )


# Lambda funksiyasi
def lambda_handler(event, context):
    news_text = event['text']
    sentiment_analysis = analyze_sentiment(news_text)
    keywords = extract_keywords(news_text)
    save_to_dynamodb(event['news_id'], sentiment_analysis, keywords)
    return {
        'statusCode': 200,
        'body': json.dumps({
            'sentiment': sentiment_analysis['sentiment'],
            'score': sentiment_analysis['sentiment_score'],
            'keywords': keywords
        })
    }
