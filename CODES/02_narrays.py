import numpy as np

# 24 hourly electricity consumption readings in kWh
consumption_kwh = np.array([
    4.2, 3.8, 3.5, 3.1, 3.4, 4.0,
    5.2, 6.1, 6.8, 7.2, 7.8, 8.5,
    8.9, 9.1, 8.7, 8.2, 7.6, 9.4,
    8.1, 7.3, 6.5, 5.8, 5.0, 4.5
])

mean_consumption = np.mean(consumption_kwh)
min_consumption = np.min(consumption_kwh)
max_consumption = np.max(consumption_kwh)

# Vectorized conversion from kWh to Wh
consumption_wh = 1000 * consumption_kwh

print(f"Daily mean consumption: {mean_consumption:.2f} kWh")
print(f"Minimum consumption: {min_consumption:.2f} kWh")
print(f"Maximum consumption: {max_consumption:.2f} kWh")
print("First six consumption readings in Wh:", consumption_wh[:6])
