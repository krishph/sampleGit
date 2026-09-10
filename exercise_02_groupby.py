"""Exercise 2: group rows and calculate summary statistics."""

import pandas as pd


sales = pd.DataFrame(
    {
        "store": ["North", "South", "North", "East", "South", "East"],
        "order_value": [125.00, 80.00, 210.00, 95.00, 160.00, 130.00],
        "items": [3, 2, 5, 1, 4, 3],
    }
)

print(sales)

# TODO: Group by store and calculate total order_value and average items.
