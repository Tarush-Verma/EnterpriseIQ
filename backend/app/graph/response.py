from app.graph.state import BusinessState

def response_node(state: BusinessState) -> dict:
    final_response = f"""
    Business Analysis
    =================

    {state["analysis"]}

    Recommendations
    ===============

    {state["recommendation"]}
    """

    return {"final_response": final_response.strip()}