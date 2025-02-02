from NLP_model import analyze_sentiment
from NLP_model import extract_keywords
from NLP_model import save_to_dynamodb
from Signal_Generation_Logic import generate_signal
from TradingView_Webhooks import send_tradingview_alert
from Alpaca_API import execute_trade

def process_news_for_trading(news_id, text, volume_spike=False):
    # Yangiliklarni tozalash va sentiment tahlili
    sentiment_result = analyze_sentiment(text)
    keywords = extract_keywords(text)

    # Signal yaratish
    signal = generate_signal(
        sentiment_result['sentiment'],
        sentiment_result['sentiment_score'],
        volume_spike
    )

    # Sentiment va hodisani saqlash
    save_to_dynamodb(news_id, sentiment_result, keywords)

    # TradingView alert yaratish
    send_tradingview_alert(signal['signal'], signal['reason'])

    # Alpaca orqali real savdo
    if signal['signal'] in ['Buy', 'Sell']:
        execute_trade(signal['signal'], "AAPL", 10)  # Misol: 10 dona Apple aksiyasi

    return {
        "news_id": news_id,
        "signal": signal,
        "keywords": keywords
    }
