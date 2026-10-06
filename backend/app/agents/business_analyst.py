from app.core.llm import model
from langchain.agents import create_agent
from app.tools.business_tools import calculate_profit, calculate_roi

business_analyst_agent = create_agent(
    model=model,
    tools=[
        calculate_profit,
        calculate_roi
    ],
    system_prompt="""
    You are the Business Analyst Agent for EnterpriseIQ AI.

    Your job is to analyze business questions and provide accurate,
    concise and useful business insights.

    Use the available tools whenever calculations are required.

    Do not guess numerical results when a tool can calculate them.
    """
)