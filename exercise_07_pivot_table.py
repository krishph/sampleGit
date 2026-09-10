"""Exercise 7: summarize values in a pivot table."""

import pandas as pd


revenue = pd.DataFrame(
    {
        "region": ["West", "West", "East", "East", "West", "East"],
        "quarter": ["Q1", "Q2", "Q1", "Q2", "Q3", "Q3"],
        "revenue": [1200, 1500, 900, 1100, 1700, 1250],
    }
)

print(revenue)

# TODO: Build a pivot table with region as rows, quarter as columns, and sum revenue.
