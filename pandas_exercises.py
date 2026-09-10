"""Ten pandas exercises with small, self-contained datasets.

Run this file to inspect the sample data, then complete each TODO in order.
"""

import pandas as pd


def exercise_1_filter_rows():
    """Filter products that are in stock and cost less than $50."""
    products = pd.DataFrame(
        {
            "product": ["Notebook", "Pen set", "Backpack", "Mug", "Desk lamp"],
            "category": ["Office", "Office", "Travel", "Kitchen", "Office"],
            "price": [12.50, 8.00, 65.00, 18.00, 42.00],
            "in_stock": [True, True, False, True, True],
        }
    )
    print("Exercise 1 sample data:\n", products, "\n")
    # TODO: Select the rows where in_stock is True and price is below 50.


def exercise_2_group_and_aggregate():
    """Find total sales and average order value for each store."""
    sales = pd.DataFrame(
        {
            "store": ["North", "South", "North", "East", "South", "East"],
            "order_value": [125.00, 80.00, 210.00, 95.00, 160.00, 130.00],
            "items": [3, 2, 5, 1, 4, 3],
        }
    )
    print("Exercise 2 sample data:\n", sales, "\n")
    # TODO: Group by store and calculate total order_value and mean items.


def exercise_3_missing_values():
    """Fill missing ratings with the overall median rating."""
    reviews = pd.DataFrame(
        {
            "customer": ["Ava", "Ben", "Chen", "Diya", "Eli", "Fox"],
            "rating": [5.0, 4.0, None, 3.0, None, 4.0],
            "reviewed_on": ["2026-01-04", "2026-01-05", "2026-01-06", "2026-01-07", "2026-01-08", "2026-01-09"],
        }
    )
    print("Exercise 3 sample data:\n", reviews, "\n")
    # TODO: Replace missing rating values with the median of rating.


def exercise_4_sort_and_top_n():
    """Find the three employees with the highest performance score."""
    employees = pd.DataFrame(
        {
            "employee": ["Mina", "Owen", "Priya", "Quinn", "Ravi"],
            "team": ["A", "B", "A", "B", "A"],
            "score": [88, 94, 91, 79, 97],
        }
    )
    print("Exercise 4 sample data:\n", employees, "\n")
    # TODO: Sort by score from highest to lowest and return the top three rows.


def exercise_5_merge_dataframes():
    """Combine order records with the customer names that placed them."""
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
    print("Exercise 5 orders:\n", orders, "\n")
    print("Exercise 5 customers:\n", customers, "\n")
    # TODO: Merge the two DataFrames so each order includes customer_name and city.


def exercise_6_work_with_dates():
    """Calculate the number of days between signup and first purchase."""
    users = pd.DataFrame(
        {
            "user": ["U1", "U2", "U3", "U4"],
            "signed_up": ["2026-02-01", "2026-02-03", "2026-02-10", "2026-02-12"],
            "first_purchase": ["2026-02-04", "2026-02-08", "2026-02-11", "2026-02-20"],
        }
    )
    print("Exercise 6 sample data:\n", users, "\n")
    # TODO: Convert both date columns to datetime and add days_to_purchase.


def exercise_7_pivot_table():
    """Create a region-by-quarter table of revenue totals."""
    revenue = pd.DataFrame(
        {
            "region": ["West", "West", "East", "East", "West", "East"],
            "quarter": ["Q1", "Q2", "Q1", "Q2", "Q3", "Q3"],
            "revenue": [1200, 1500, 900, 1100, 1700, 1250],
        }
    )
    print("Exercise 7 sample data:\n", revenue, "\n")
    # TODO: Build a pivot table with region as rows, quarter as columns, and sum revenue.


def exercise_8_clean_text():
    """Normalize city names and count customers by city."""
    contacts = pd.DataFrame(
        {
            "name": ["Nora", "Sam", "Tess", "Uma", "Vik"],
            "city": [" new york", "NEW YORK", "Boston ", "boston", "Chicago"],
        }
    )
    print("Exercise 8 sample data:\n", contacts, "\n")
    # TODO: Strip whitespace, make city names title case, then count customers per city.


def exercise_9_remove_duplicates():
    """Keep the latest status update for each ticket."""
    updates = pd.DataFrame(
        {
            "ticket_id": ["T1", "T2", "T1", "T3", "T2"],
            "updated_at": ["2026-03-01", "2026-03-01", "2026-03-03", "2026-03-02", "2026-03-04"],
            "status": ["open", "open", "closed", "pending", "closed"],
        }
    )
    print("Exercise 9 sample data:\n", updates, "\n")
    # TODO: Convert updated_at to datetime and keep the newest row per ticket_id.


def exercise_10_rolling_average():
    """Calculate a three-day rolling average of website visits."""
    traffic = pd.DataFrame(
        {
            "date": pd.date_range("2026-03-01", periods=7, freq="D"),
            "visits": [120, 150, 135, 180, 210, 190, 230],
        }
    )
    print("Exercise 10 sample data:\n", traffic, "\n")
    # TODO: Add a three_day_average column using visits.rolling(3).mean().


if __name__ == "__main__":
    exercise_1_filter_rows()
    exercise_2_group_and_aggregate()
    exercise_3_missing_values()
    exercise_4_sort_and_top_n()
    exercise_5_merge_dataframes()
    exercise_6_work_with_dates()
    exercise_7_pivot_table()
    exercise_8_clean_text()
    exercise_9_remove_duplicates()
    exercise_10_rolling_average()