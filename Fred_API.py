import requests
import json

# API settings
FRED_API_KEY = "Your_Fred_API_key"  # Replace with your API key
SERIES_IDS = ["UNRATE", "CPIAUCSL", "PCE", "DGS10", "DGS2"]  # Economic indicators
BASE_URL = "https://api.stlouisfed.org/fred/series/observations"
N = 5  # Number of most recent data points to fetch


# Function to fetch data from API
def get_fred_data(series_id):
    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json"
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        fred_data = response.json()
        # Return the last N observations
        return fred_data["observations"][-N:]
    else:
        print(f"Error: Could not fetch data for {series_id}! Status code: {response.status_code}")
        return []


# Dictionary to store data for all series
fred_data_all = {}

# Fetch data for each indicator
for series in SERIES_IDS:
    observations = get_fred_data(series)
    fred_data_all[series] = observations  # Store the data for each series in the dictionary

    print(f"\n📌 Last {N} data points for {series}:")
    for obs in observations:
        print(f"{obs['date']}: {obs['value']}")

# Save the data to a JSON file
with open("Fred_data.json", "w") as file:
    json.dump(fred_data_all, file, indent=4)

print("\n✅ FRED data has been saved to 'Fred_data.json'.")
