"""Exercise 3: fill missing values with a calculated value."""

import pandas as pd


reviews = pd.DataFrame(
    {
        "customer": ["Ava", "Ben", "Chen", "Diya", "Eli", "Fox"],
        "rating": [5.0, 4.0, None, 3.0, None, 4.0],
        "reviewed_on": [
            "2026-01-04",
            "2026-01-05",
            "2026-01-06",
            "2026-01-07",
            "2026-01-08",
            "2026-01-09",
        ],
    }
)

print(reviews)

# TODO: Replace missing rating values with the median rating.
