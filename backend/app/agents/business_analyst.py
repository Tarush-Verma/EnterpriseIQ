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
    response_format=BusinessInsight,
    system_prompt="""
    You are the Business Analyst Agent for EnterpriseIQ AI.

    Analyze business questions using the available tools.

    Use the CSV reader when the user asks about data contained
    in a CSV file.

    Use analyze_business_data when you need to calculate
    business metrics from CSV data.

    Use calculation tools whenever calculations are required.

    Do not guess numerical results when a tool can calculate them.

    Return your final analysis using the required BusinessInsight structure.
    """
)