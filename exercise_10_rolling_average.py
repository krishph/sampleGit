"""Exercise 10: calculate a rolling average."""

import pandas as pd


traffic = pd.DataFrame(
    {
        "date": pd.date_range("2026-03-01", periods=7, freq="D"),
        "visits": [120, 150, 135, 180, 210, 190, 230],
    }
)

print(traffic)

# TODO: Add a three_day_average column using visits.rolling(3).mean().
