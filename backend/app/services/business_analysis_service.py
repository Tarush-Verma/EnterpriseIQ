from app.agents.business_analyst import business_analyst_agent
from app.core.structured_model import structured_model
from app.tools.csv_tools import analyze_business_data


def analyze_business_question(question: str) -> dict:

    file_path = "../datasets/business_data.csv"

    # 1. Get exact deterministic metrics
    metrics = analyze_business_data.invoke({
        "file_path": file_path
    })

    # 2. Let the agent reason about the business data
    result = business_analyst_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": f"""
                    Analyze the business data in
                    {file_path}.

                    Here are the exact calculated metrics:

                    {metrics}

                    Question:
                    {question}

                    Give a concise business analysis and recommendation.
                    """
                }
            ]
        }
    )

    business_analysis = result["messages"][-1].content

    # 3. Convert the analysis into the final structured response
    structured_result = structured_model.invoke(
        f"""
        Create a BusinessInsight from the following information.

        IMPORTANT:
        The numerical values below are calculated deterministically.
        Do not change or recalculate them.

        Exact metrics:
        Total revenue: {metrics.total_revenue}
        Total expenses: {metrics.total_expenses}
        Total profit: {metrics.total_profit}
        Profit margin: {metrics.profit_margin}
        Average monthly revenue: {metrics.average_monthly_revenue}
        Average monthly profit: {metrics.average_monthly_profit}
        Highest revenue month: {metrics.highest_revenue_month}
        Highest profit month: {metrics.highest_profit_month}
        Lowest profit month: {metrics.lowest_profit_month}

        Business analysis:
        {business_analysis}

        Use the exact total profit and profit margin values
        provided above.
        """
    )

    return {
        "metrics": metrics,
        "analysis": business_analysis,
        "structured_response": structured_result,
    }