"""Exercise 8: clean text values and count categories."""

import pandas as pd


contacts = pd.DataFrame(
    {
        "name": ["Nora", "Sam", "Tess", "Uma", "Vik"],
        "city": [" new york", "NEW YORK", "Boston ", "boston", "Chicago"],
    }
)

print(contacts)

# TODO: Strip whitespace, title-case city names, and count customers per city.
