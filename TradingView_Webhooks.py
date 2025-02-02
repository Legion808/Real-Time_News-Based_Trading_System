import requests

TRADINGVIEW_WEBHOOK_URL = "https://hooks.tradingview.com/{YourWebhookEndpoint}"


def send_tradingview_alert(signal, reason=None):
    payload = {
        "text": f"Trade Signal: {signal}",
        "detail": reason if reason else "Check market for further analysis"
    }
    response = requests.post(TRADINGVIEW_WEBHOOK_URL, json=payload)
    return response.status_code, response.text
