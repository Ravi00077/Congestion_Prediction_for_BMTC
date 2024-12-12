import numpy as np
import pandas as pd
import random

n_samples = 1000  # Number of samples

# Generate synthetic data
data = {
    "Route_ID": np.random.randint(1, 20, n_samples),
    "Time": [f"{random.randint(0, 23):02}:{random.randint(0, 59):02}" for _ in range(n_samples)],
    "Day": np.random.choice(["Weekday", "Weekend"], n_samples),
    "Weather": np.random.choice(["Clear", "Rainy", "Foggy"], n_samples, p=[0.7, 0.2, 0.1]),
    "Traffic_Volume": np.random.randint(100, 2000, n_samples),
}

# Create initial DataFrame
df_traffic = pd.DataFrame(data)

# Define congestion levels based on other features
def define_congestion(row):
    volume = row["Traffic_Volume"]
    weather = row["Weather"]
    day = row["Day"]
    time = int(row["Time"].split(":")[0])  # Extract hour from time

    # Base congestion level
    if volume > 1500:
        congestion = "High"
    elif 800 <= volume <= 1500:
        congestion = "Medium"
    else:
        congestion = "Low"

    # Adjust based on weather
    if weather in ["Rainy", "Foggy"]:
        if congestion == "Medium":
            congestion = "High"
        elif congestion == "Low":
            congestion = "Medium"

    # Adjust based on day
    if day == "Weekend" and congestion == "High":
        congestion = "Medium"

    # Adjust based on time (e.g., peak hours 7-9 AM and 5-7 PM)
    if 7 <= time <= 9 or 17 <= time <= 19:
        if congestion == "Medium":
            congestion = "High"
        elif congestion == "Low":
            congestion = "Medium"

    return congestion

# Apply function to define congestion levels
df_traffic["Congestion_Level"] = df_traffic.apply(define_congestion, axis=1)

# Display the DataFrame
print(df_traffic.head())


# Save to CSV
df_traffic.to_csv("synthetic_traffic_data.csv", index=False)
