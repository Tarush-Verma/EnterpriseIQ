from app.core.llm import model
from langchain.agents import create_agent
from app.models.business_insight import BusinessInsight
from app.tools.business_tools import calculate_profit, calculate_roi
from app.tools.csv_tools import read_csv, analyze_business_data

business_analyst_agent = create_agent(
    model=model,
    tools=[
        calculate_profit,
        calculate_roi,
        read_csv,
        analyze_business_data
    ],
    system_prompt="""
    You are the Business Analyst Agent for EnterpriseIQ AI.

    Analyze business questions using the available tools.

    Use the CSV reader when the user asks about data
    contained in a CSV file.

    Use analyze_business_data when you need to calculate
    business metrics from CSV data.

    Use calculation tools whenever calculations are required.

    Do not guess numerical results.

    Give a concise business analysis and recommendation
    based on the tool results.

    Avoid making claims that require information not present
    in the provided data.

    Do not assume industry benchmarks, market conditions,
    or seasonality unless the data explicitly supports them.

    Clearly distinguish between observed facts and possible explanations.
    """
)