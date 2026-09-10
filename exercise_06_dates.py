"""Exercise 6: convert dates and calculate a date difference."""

import pandas as pd


users = pd.DataFrame(
    {
        "user": ["U1", "U2", "U3", "U4"],
        "signed_up": ["2026-02-01", "2026-02-03", "2026-02-10", "2026-02-12"],
        "first_purchase": ["2026-02-04", "2026-02-08", "2026-02-11", "2026-02-20"],
    }
)

print(users)

# TODO: Convert both date columns to datetime and add days_to_purchase.
