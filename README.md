[README (9).md](https://github.com/user-attachments/files/32117510/README.9.md)
# Expense Tracker CLI & Data Visualization Application

A Python-based command-line tool for managing, summarizing, and visualizing personal expenses. It leverages `pandas` and `numpy` for data manipulation and analysis, with `matplotlib` and `seaborn` providing interactive visualization graphics.

## Features

- **Data Management & Input Validation**: Persists expense logs in a local CSV file (`expenses.csv`). Validates dates (YYYY-MM-DD), ensures amounts are numeric/positive, and enforces predefined category types (`Food`, `Transport`, `Utilities`, `Entertainment`, `Other`).
- **Data Processing & Filtering**: Uses Pandas DataFrames and NumPy arrays to clean data, compute aggregate metrics, and filter transactions by category or amount.
- **Summary Reports**: Calculates spending totals, averages, maximum/minimum expenses, and identifies top-spending categories and time periods.
- **Data Visualization Dashboard**: Displays a 2x2 grid of charts:
  1. Bar Chart: Category expense totals.
  2. Line Plot: Spending trends over time.
  3. Pie Chart: Proportional distribution of categories.
  4. Histogram: Distribution frequency of transaction amounts.

## Project Structure

- `ExpenseTracker.py` — Core script containing the `ExpenseTracker` class, sample data generator, visualization pipeline, and interactive menu.
- `expenses.csv` — CSV file storing transaction records (generated automatically if missing).

## Sample Output

### 1. Adding a New Expense & Viewing the Summary

Adding a new entry ("Team lunch", $1000, Food) and checking the running total/average.

```
=== EXPENSE TRACKER MENU ===
1. Add New Expense
2. View Expense Summary
3. Generate Full Report
4. Filter Expenses
5. View Visualizations (Charts)
6. Exit
Enter option (1-6): 1

--- Add Expense ---
Enter date (YYYY-MM-DD): 2024-07-18
Enter amount: 1000
Enter category (Food, Transport, Utilities, Entertainment, Other): Food
Enter description: Team lunch
[+] Expense added successfully!

=== EXPENSE TRACKER MENU ===
1. Add New Expense
2. View Expense Summary
3. Generate Full Report
4. Filter Expenses
5. View Visualizations (Charts)
6. Exit
Enter option (1-6): 2

--- Summary Metrics ---
Total Spent   : $5908.00
Average Spend : $347.53
-----------------------
```

### 2. Generating the Full Expense Report

A detailed breakdown of total spending, category-wise aggregates, and top spending category/period.

```
=== EXPENSE TRACKER MENU ===
1. Add New Expense
2. View Expense Summary
3. Generate Full Report
4. Filter Expenses
5. View Visualizations (Charts)
6. Exit
Enter option (1-6): 3

========================================
        EXPENSE SUMMARY REPORT
========================================
Total Entries Recorded : 17
Total Spending          : $5908.00
Average Expense         : $347.53
Max Single Expense      : $1000.00
Min Single Expense      : $12.00

--- Spending by Category ---
                Total ($)  Average ($)  Transactions
Category
Entertainment      240.0        80.00             3
Food               5130.5      641.31             8
Transport            67.5        22.50             3
Utilities           470.0       156.67             3

Top Spending Category : Food ($5130.50)
Top Spending Period   : 2024-07 ($5000.00)
========================================
```

### 3. Filtering Expenses

Viewing all recorded transactions (filter skipped) with the derived `Month` column.

```
=== EXPENSE TRACKER MENU ===
1. Add New Expense
2. View Expense Summary
3. Generate Full Report
4. Filter Expenses
5. View Visualizations (Charts)
6. Exit
Enter option (1-6): 4

--- Filter Expenses ---
Enter category to filter (press Enter to skip):

Filtered Results:
         Date   Amount      Category          Description    Month
0  2026-01-05     45.5          Food     Grocery shopping  2026-01
1  2026-01-12     12.0     Transport           Bus ticket  2026-01
2  2026-01-15    120.0     Utilities    Electricity bill   2026-01
3  2026-01-20     65.0  Entertainment        Movie night   2026-01
4  2026-02-02    150.0     Utilities        Internet bill  2026-02
5  2026-02-10     30.0          Food  Lunch with friends   2026-02
6  2026-02-14     85.0  Entertainment      Concert ticket  2026-02
7  2026-02-22     40.0     Transport         Gas fill up   2026-02
8  2026-03-01    200.0     Utilities          Water bill   2026-03
9  2026-03-05     55.0          Food              Dinner   2026-03
10 2026-03-12     15.5     Transport          Metro pass   2026-03
11 2026-03-18     90.0  Entertainment        Board games   2026-03
12 2024-07-18   1000.0          Food          Team lunch   2024-07
...
```

### 4. Generating Visualizations & Exiting

Launching the 2x2 chart dashboard and exiting the program.

```
=== EXPENSE TRACKER MENU ===
1. Add New Expense
2. View Expense Summary
3. Generate Full Report
4. Filter Expenses
5. View Visualizations (Charts)
6. Exit
Enter option (1-6): 5

Generating charts...

=== EXPENSE TRACKER MENU ===
1. Add New Expense
2. View Expense Summary
3. Generate Full Report
4. Filter Expenses
5. View Visualizations (Charts)
6. Exit
Enter option (1-6): 6
Exiting program. Goodbye!
```

---

**Author:** Pankti Patel
