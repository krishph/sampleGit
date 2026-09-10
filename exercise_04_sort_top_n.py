"""Exercise 4: sort rows and select the top results."""

import pandas as pd


employees = pd.DataFrame(
    {
        "employee": ["Mina", "Owen", "Priya", "Quinn", "Ravi"],
        "team": ["A", "B", "A", "B", "A"],
        "score": [88, 94, 91, 79, 97],
    }
)

print(employees)

# TODO: Sort by score from highest to lowest and select the top three rows.
