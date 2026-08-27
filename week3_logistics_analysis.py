"""
Week 3 - Advanced Data Analysis and Visualization in Logistics
This script simulates a logistics dataset, performs EDA, creates visualizations,
and prints summary tables.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
n = 500

regions = rng.choice(["North", "South", "East", "West"], n, p=[.25,.25,.23,.27])
transport = rng.choice(["Road", "Rail", "Air"], n, p=[.62,.23,.15])
priority = rng.choice(["Standard", "Express"], n, p=[.72,.28])
distance = np.clip(rng.gamma(2.6, 170, n) + 50, 60, 1400)
volume = np.clip(rng.lognormal(3.0, .55, n), 5, 150)
weight = np.clip(volume * rng.uniform(.65, 1.9, n), 5, 240)

base_days = {"Road":3.8, "Rail":5.2, "Air":1.5}
delivery = (
    np.array([base_days[t] for t in transport])
    + distance / np.array([260 if t=="Road" else 190 if t=="Rail" else 700 for t in transport])
    + rng.normal(0, .75, n)
    + np.where(priority=="Express", -.8, 0)
    + np.where(regions=="East", .35, 0)
)
delivery = np.clip(delivery, .5, None)

cost_per_km = {"Road":2.9, "Rail":1.75, "Air":8.4}
cost = (
    distance * np.array([cost_per_km[t] for t in transport])
    + volume * rng.uniform(18, 38, n)
    + weight * rng.uniform(2.0, 5.5, n)
    + np.where(priority=="Express", 650, 0)
    + rng.normal(0, 380, n)
)
cost = np.clip(cost, 500, None)

delay_prob = np.clip(
    .08 + .00055*distance + .035*(delivery>7)
    + .05*(regions=="East") + .025*(transport=="Rail"), .03, .75
)
delayed = rng.random(n) < delay_prob

df = pd.DataFrame({
    "Region": regions,
    "Transport_Mode": transport,
    "Priority": priority,
    "Distance_km": distance,
    "Shipment_Volume_units": volume,
    "Weight_kg": weight,
    "Delivery_Time_days": delivery,
    "Transport_Cost_INR": cost,
    "Delayed": np.where(delayed, "Yes", "No")
})

print(df.describe(include="all"))
print("\\nCorrelation matrix:")
print(df.select_dtypes("number").corr())

mode_summary = df.groupby("Transport_Mode").agg(
    Avg_Delivery_Days=("Delivery_Time_days","mean"),
    Avg_Cost_INR=("Transport_Cost_INR","mean"),
    Delay_Rate=("Delayed", lambda x: (x=="Yes").mean()*100)
)
print("\\nMode summary:")
print(mode_summary)

plt.figure()
plt.hist(df["Delivery_Time_days"], bins=25, edgecolor="black")
plt.title("Distribution of Delivery Time")
plt.xlabel("Days")
plt.ylabel("Shipments")
plt.show()

plt.figure()
for mode in ["Road","Rail","Air"]:
    d = df[df["Transport_Mode"] == mode]
    plt.scatter(d["Distance_km"], d["Transport_Cost_INR"], label=mode, alpha=.55)
plt.xlabel("Distance (km)")
plt.ylabel("Transport Cost (INR)")
plt.title("Distance vs Transport Cost")
plt.legend()
plt.show()
