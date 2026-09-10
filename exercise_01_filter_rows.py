"""Exercise 1: filter rows with boolean conditions."""

import pandas as pd


products = pd.DataFrame(
    {
        "product": ["Notebook", "Pen set", "Backpack", "Mug", "Desk lamp"],
        "category": ["Office", "Office", "Travel", "Kitchen", "Office"],
        "price": [12.50, 8.00, 65.00, 18.00, 42.00],
        "in_stock": [True, True, False, True, True],
    }
)

print(products)

# TODO: Select products that are in stock and cost less than 50.
