"""Exercise 9: remove duplicates while keeping the newest record."""

import pandas as pd


updates = pd.DataFrame(
    {
        "ticket_id": ["T1", "T2", "T1", "T3", "T2"],
        "updated_at": [
            "2026-03-01",
            "2026-03-01",
            "2026-03-03",
            "2026-03-02",
            "2026-03-04",
        ],
        "status": ["open", "open", "closed", "pending", "closed"],
    }
)

print(updates)

# TODO: Convert updated_at to datetime and keep the newest row per ticket_id.
