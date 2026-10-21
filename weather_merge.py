
import pandas as pd
import requests
import time

# Input: corrected flight dataset
flights = pd.read_csv(r"D:\DMW assignment\indian_dataset\data\flights_dates_corrected.csv")
flights["FLIGHT_DATETIME"] = pd.to_datetime(
    flights["FLIGHT_DATETIME"], errors="coerce"
)

# Approximate coordinates of the departure airports
airports = {
    "AMD": (23.077, 72.634),   # Ahmedabad
    "BBI": (20.244, 85.818),   # Bhubaneswar
    "BLR": (13.198, 77.706),   # Bengaluru
    "BOM": (19.090, 72.866),   # Mumbai
    "CCU": (22.655, 88.447),   # Kolkata
    "COK": (10.152, 76.402),   # Kochi
    "DEL": (28.556, 77.100),   # Delhi
    "GOI": (15.381, 73.831),   # Goa
    "HYD": (17.240, 78.429),   # Hyderabad
    "IXC": (30.674, 76.789),   # Chandigarh
    "JAI": (26.824, 75.812),   # Jaipur
    "LKO": (26.761, 80.889),   # Lucknow
    "MAA": (12.994, 80.171),   # Chennai
    "PAT": (25.591, 85.088),   # Patna
    "PNQ": (18.582, 73.920),   # Pune
}

variables = [
    "temperature_2m",
    "relative_humidity_2m",
    "precipitation",
    "rain",
    "cloud_cover",
    "wind_speed_10m",
    "wind_direction_10m",
    "pressure_msl",
    "weather_code",
]

url = "https://archive-api.open-meteo.com/v1/archive"
weather_frames = []

for code in sorted(flights["ORIGIN_AIRPORT"].dropna().unique()):
    if code not in airports:
        print(f"Skipping unknown airport: {code}")
        continue

    latitude, longitude = airports[code]

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": "2024-01-01",
        "end_date": "2024-12-31",
        "hourly": ",".join(variables),
        "timezone": "Asia/Kolkata",
        "wind_speed_unit": "kmh",
    }

    response = requests.get(url, params=params, timeout=60)
    response.raise_for_status()
    result = response.json()

    hourly = pd.DataFrame(result["hourly"])
    hourly = hourly.rename(columns={"time": "WEATHER_DATETIME"})
    hourly["WEATHER_DATETIME"] = pd.to_datetime(
        hourly["WEATHER_DATETIME"]
    )
    hourly["ORIGIN_AIRPORT"] = code

    weather_frames.append(hourly)
    print(f"Downloaded weather for {code}: {len(hourly)} hourly records")
    time.sleep(0.3)

weather = pd.concat(weather_frames, ignore_index=True)

# Save weather independently for traceability
weather.to_csv("weather_india_2024.csv", index=False)

# Match each flight to weather for its scheduled departure hour
flights["WEATHER_DATETIME"] = (
    flights["FLIGHT_DATETIME"].dt.floor("h")
)

merged = flights.merge(
    weather,
    on=["ORIGIN_AIRPORT", "WEATHER_DATETIME"],
    how="left",
    validate="many_to_one",
    indicator=True,
)

print("\nWeather merge results:")
print(merged["_merge"].value_counts(dropna=False))
print("Total flights:", len(merged))
print("Missing weather rows:", merged[variables].isna().all(axis=1).sum())

merged.drop(columns=["_merge"]).to_csv(
    "flights_with_weather_2024.csv", index=False
)

print("Saved weather_india_2024.csv")
print("Saved flights_with_weather_2024.csv")
