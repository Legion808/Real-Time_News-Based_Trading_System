def generate_signal(sentiment, sentiment_score, volume_spike=False):
    if volume_spike:
        return {
            "signal": "Alert",
            "reason": "Possible insider trading activity detected",
            "recommendation": "Monitor market activity closely"
        }
    elif sentiment == "bullish" and sentiment_score > 0.75:
        return {
            "signal": "Buy",
            "reason": "Strong bullish sentiment",
            "recommendation": "Consider investing in leveraged assets"
        }
    elif sentiment == "bearish" and sentiment_score < -0.75:
        return {
            "signal": "Sell",
            "reason": "Strong bearish sentiment",
            "recommendation": "Reduce exposure to risky assets"
        }
    else:
        return {
            "signal": "Hold",
            "reason": "Neutral/low sentiment impact",
            "recommendation": "No immediate action required"
        }
