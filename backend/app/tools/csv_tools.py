import csv 

from langchain_core.tools import tool

@tool
def read_csv(file_path: str) -> list[dict]:
    """Read a business CSV file and return its rows with numeric values converted."""

    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        rows = []

        for row in reader:
            converted_row = {}

            for key, value in row.items():
                try:
                    converted_row[key] = float(value)
                except (ValueError, TypeError):
                    converted_row[key] = value

            rows.append(converted_row)

        return rows


@tool
def analyze_business_data(file_path: str) -> dict:
    """Analyze business data and calculate key financial metrics."""

    rows = read_csv.invoke({"file_path": file_path})

    total_revenue = sum(row["revenue"] for row in rows)
    total_expenses = sum(row["expenses"] for row in rows)

    total_profit = total_revenue - total_expenses 

    if total_revenue == 0:
        profit_margin = 0 
    else:
        profit_margin = (total_profit / total_revenue) * 100

    average_revenue = total_revenue / len(rows)

    highest_revenue_month = max(
        rows,
        key= lambda row: row["revenue"]
    )["month"]

    highest_profit_month = max(
        rows,
        key=lambda row: row["revenue"] - row["expenses"]
    )["month"]

    lowest_profit_month = min(
        rows,
        key= lambda row: row["revenue"] - row["expenses"]
    )["month"]

    average_monthly_profit = total_profit / len(rows)

    return {
        "total_revenue": total_revenue,
        "total_expenses": total_expenses,
        "total_profit": total_profit,
        "profit_margin": round(profit_margin, 2),
        "average_monthly_revenue": round(average_revenue, 2),
        "highest_revenue_month": highest_revenue_month,
        "highest_profit_month": highest_profit_month,
        "lowest_profit_month": lowest_profit_month,
        "average_monthly_profit": round(average_monthly_profit, 2),
    }