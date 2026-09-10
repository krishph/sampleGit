"""Exercise 5: merge related DataFrames."""

import pandas as pd


orders = pd.DataFrame(
    {
        "order_id": [101, 102, 103, 104],
        "customer_id": [1, 2, 1, 3],
        "amount": [45.00, 72.00, 18.00, 110.00],
    }
)
customers = pd.DataFrame(
    {
        "customer_id": [1, 2, 3],
        "customer_name": ["Ari", "Blair", "Casey"],
        "city": ["Austin", "Boston", "Chicago"],
    }
)

print("Orders:\n", orders)
print("Customers:\n", customers)

# TODO: Merge the DataFrames so each order includes customer_name and city.
