from langchain_core.tools import tool 

@tool
def calculate_profit(revenue: float , expenses: float) -> dict :
    """Calculate business profit and profit margin from revenue and expenses."""
    
    profit = revenue - expenses 

    if revenue == 0:
        profit_margin = 0 
    else:
        profit_margin = (profit / revenue) * 100 

    return {
        "revenue" : revenue,
        "expenses" : expenses,
        "profit" : profit,
        "profit_margin" : round(profit_margin,2),
    }

@tool
def calculate_roi(investment: float , return_amount: float) -> float:
    """Calculate return on investment (ROI) as a percentage."""

    if investment == 0:
        return 0 

    roi = ((return_amount - investment) / investment) * 100 

    return round(roi,2)