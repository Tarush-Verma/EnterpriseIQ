from pydantic import BaseModel

class BusinessMetrics(BaseModel):
    total_revenue: float
    total_expenses: float
    total_profit: float
    profit_margin: float
    average_monthly_revenue: float
    average_monthly_profit: float
    highest_revenue_month: str
    highest_profit_month: str
    lowest_profit_month: str    