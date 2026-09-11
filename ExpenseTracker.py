import os
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set style for plots
sns.set_theme(style="whitegrid")


# ==========================================
# Helper Function: Create Sample CSV
# ==========================================
def create_sample_csv(filename="expenses.csv"):
    """Generates a sample expenses CSV file if it doesn't already exist."""
    if not os.path.exists(filename):
        sample_data = {
            "Date": [
                "2026-01-05",
                "2026-01-12",
                "2026-01-15",
                "2026-01-20",
                "2026-02-02",
                "2026-02-10",
                "2026-02-14",
                "2026-02-22",
                "2026-03-01",
                "2026-03-05",
                "2026-03-12",
                "2026-03-18",
            ],
            "Amount": [
                45.50,
                12.00,
                120.00,
                65.00,
                150.00,
                30.00,
                85.00,
                40.00,
                200.00,
                55.00,
                15.50,
                90.00,
            ],
            "Category": [
                "Food",
                "Transport",
                "Utilities",
                "Entertainment",
                "Utilities",
                "Food",
                "Entertainment",
                "Transport",
                "Utilities",
                "Food",
                "Transport",
                "Entertainment",
            ],
            "Description": [
                "Grocery shopping",
                "Bus ticket",
                "Electricity bill",
                "Movie night",
                "Internet bill",
                "Lunch with friends",
                "Concert ticket",
                "Gas fill up",
                "Water bill",
                "Dinner",
                "Metro pass",
                "Board games",
            ],
        }
        df = pd.DataFrame(sample_data)
        df.to_csv(filename, index=False)
        print(f"Sample dataset '{filename}' created successfully.\n")


# ==========================================
# Section 1 & 2: OOP & Input Validation
# ==========================================
class ExpenseTracker:

    def __init__(self, filename="expenses.csv"):
        self.filename = filename
        self.valid_categories = [
            "Food",
            "Transport",
            "Utilities",
            "Entertainment",
            "Other",
        ]
        self.df = self.load_data()

    def load_data(self):
        """Loads and cleans expense data using Pandas."""
        try:
            df = pd.read_csv(self.filename)

            # Data cleaning
            df["Date"] = pd.to_datetime(df["Date"])
            df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
            df = df.dropna(subset=["Amount", "Date", "Category"])

            return df
        except Exception as e:
            print(f"Error loading CSV file: {e}")
            return pd.DataFrame(
                columns=["Date", "Amount", "Category", "Description"]
            )

    def validate_input(self, date_str, amount, category):
        """Validates input data with simple control structures."""
        # 1. Validate Date format
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print(
                "[-] Invalid date format! Please use YYYY-MM-DD (e.g., 2026-03-15)."
            )
            return False

        # 2. Validate Amount > 0
        if amount <= 0:
            print("[-] Amount must be greater than zero!")
            return False

        # 3. Validate Category
        if category.capitalize() not in self.valid_categories:
            print(
                f"[-] Invalid category! Options are: {', '.join(self.valid_categories)}"
            )
            return False

        return True

    def add_expense(self, date, amount, category, description):
        """Logs new expense after validating user inputs."""
        category_formatted = category.capitalize()

        if not self.validate_input(date, amount, category_formatted):
            print("Failed to add expense due to validation errors.")
            return

        new_row = pd.DataFrame(
            [
                {
                    "Date": pd.to_datetime(date),
                    "Amount": float(amount),
                    "Category": category_formatted,
                    "Description": description,
                }
            ]
        )

        # Append new expense to DataFrame and save back to CSV
        self.df = pd.concat([self.df, new_row], ignore_index=True)
        self.df.to_csv(self.filename, index=False)
        print("[+] Expense added successfully!")

    def get_summary(self):
        """Provides a summary using NumPy for numerical calculations."""
        amounts = self.df["Amount"].to_numpy()

        if len(amounts) == 0:
            print("No expense data available.")
            return

        total_expense = np.sum(amounts)
        avg_expense = np.mean(amounts)

        print("\n--- Summary Metrics ---")
        print(f"Total Spent   : ${total_expense:.2f}")
        print(f"Average Spend : ${avg_expense:.2f}")
        print("-----------------------\n")

    def filter_expenses(
        self, category=None, min_amount=None, max_amount=None
    ):
        """Filters expenses by category or amount range."""
        filtered = self.df.copy()

        if category:
            filtered = filtered[
                filtered["Category"].str.lower() == category.lower()
            ]

        if min_amount is not None:
            filtered = filtered[filtered["Amount"] >= min_amount]

        if max_amount is not None:
            filtered = filtered[filtered["Amount"] <= max_amount]

        return filtered

    def generate_report(self):
        """Outputs key metrics and grouped category insights using Pandas & NumPy."""
        print("\n" + "=" * 40)
        print("        EXPENSE SUMMARY REPORT        ")
        print("=" * 40)

        amounts = self.df["Amount"].to_numpy()
        print(f"Total Entries Recorded : {len(amounts)}")
        print(f"Total Spending         : ${np.sum(amounts):.2f}")
        print(f"Average Expense        : ${np.mean(amounts):.2f}")
        print(f"Max Single Expense     : ${np.max(amounts):.2f}")
        print(f"Min Single Expense     : ${np.min(amounts):.2f}")

        # Pandas grouping by Category
        print("\n--- Spending by Category ---")
        cat_summary = self.df.groupby("Category")["Amount"].agg(
            ["sum", "mean", "count"]
        )
        cat_summary.columns = ["Total ($)", "Average ($)", "Transactions"]
        print(cat_summary.round(2))

        # Identify top spending category
        top_cat = cat_summary["Total ($)"].idxmax()
        top_val = cat_summary["Total ($)"].max()
        print(
            f"\nTop Spending Category : {top_cat} (${top_val:.2f})"
        )

        # Identify top spending month
        self.df["Month"] = self.df["Date"].dt.to_period("M")
        monthly_summary = self.df.groupby("Month")["Amount"].sum()
        top_month = monthly_summary.idxmax()
        print(
            f"Top Spending Period   : {top_month} (${monthly_summary[top_month]:.2f})"
        )
        print("=" * 40 + "\n")


# ==========================================
# Section 4: Visualizations
# ==========================================
def plot_visualizations(tracker):
    """Generates all 4 requested plots using Matplotlib and Seaborn."""
    df = tracker.df.copy()

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Expense Analysis Dashboard", fontsize=16, fontweight="bold")

    # 1. Bar Chart: Total expenses by category (Fixed Warning)
    cat_totals = df.groupby("Category")["Amount"].sum().reset_index()
    sns.barplot(
        data=cat_totals,
        x="Category",
        y="Amount",
        hue="Category",
        legend=False,
        ax=axes[0, 0],
        palette="viridis",
    )
    axes[0, 0].set_title("Total Expenses by Category")
    axes[0, 0].set_ylabel("Total Amount ($)")

    # 2. Line Graph: Spending trends over time
    daily_spend = df.groupby("Date")["Amount"].sum().reset_index()
    sns.lineplot(
        data=daily_spend,
        x="Date",
        y="Amount",
        marker="o",
        color="teal",
        ax=axes[0, 1],
    )
    axes[0, 1].set_title("Spending Trends Over Time")
    axes[0, 1].set_ylabel("Amount ($)")
    axes[0, 1].tick_params(axis="x", rotation=30)

    # 3. Pie Chart: Proportional spending distribution by category
    axes[1, 0].pie(
        cat_totals["Amount"],
        labels=cat_totals["Category"],
        autopct="%1.1f%%",
        startangle=140,
        colors=sns.color_palette("Set2"),
    )
    axes[1, 0].set_title("Spending Distribution by Category")

    # 4. Histogram: Frequency of expense amounts
    sns.histplot(
        df["Amount"], bins=6, kde=True, color="purple", ax=axes[1, 1]
    )
    axes[1, 1].set_title("Frequency of Expense Amounts")
    axes[1, 1].set_xlabel("Expense Amount ($)")
    axes[1, 1].set_ylabel("Frequency")

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()


# ==========================================
# Main Execution / Interactive Console
# ==========================================
def main():
    # Setup data file
    create_sample_csv("expenses.csv")

    # Initialize Tracker
    tracker = ExpenseTracker("expenses.csv")

    # Display console menu
    while True:
        print("\n=== EXPENSE TRACKER MENU ===")
        print("1. Add New Expense")
        print("2. View Expense Summary")
        print("3. Generate Full Report")
        print("4. Filter Expenses")
        print("5. View Visualizations (Charts)")
        print("6. Exit")

        choice = input("Enter option (1-6): ").strip()

        if choice == "1":
            print("\n--- Add Expense ---")
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                amount = float(input("Enter amount: "))
            except ValueError:
                print("[-] Invalid amount numerical input!")
                continue
            category = input(
                "Enter category (Food, Transport, Utilities, Entertainment, Other): "
            )
            desc = input("Enter description: ")

            tracker.add_expense(date, amount, category, desc)

        elif choice == "2":
            tracker.get_summary()

        elif choice == "3":
            tracker.generate_report()

        elif choice == "4":
            print("\n--- Filter Expenses ---")
            cat_input = input("Enter category to filter (press Enter to skip): ")
            filtered = tracker.filter_expenses(
                category=cat_input if cat_input else None
            )
            print("\nFiltered Results:")
            print(filtered)

        elif choice == "5":
            print("\nGenerating charts...")
            plot_visualizations(tracker)

        elif choice == "6":
            print("Exiting program. Goodbye!")
            break

        else:
            print("[-] Invalid choice! Please select 1-6.")


if __name__ == "__main__":
    main()