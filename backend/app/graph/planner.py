from app.core.llm import model
from app.graph.state import BusinessState

def planner_node(state: BusinessState) -> dict:
    question = state["question"]

    response = model.invoke(
        f"""
    You are the Planner for EnterpriseIQ AI.

    Create a concise plan of 3-5 steps to answer
    the user's business question.

    Use only the kinds of data available or requested.
    Do not assume that industry benchmarks, historical
    periods, or additional metrics are available.

    Do not answer the question yet.
    Return only the plan.

    User question:
    {question}
    """
    )

    return {"plan": response.content}