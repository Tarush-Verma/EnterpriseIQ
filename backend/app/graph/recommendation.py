
from app.core.llm import model
from app.graph.state import BusinessState


def recommendation_node(state: BusinessState) -> dict:
    response = model.invoke(
        f"""
You are the Recommendation component of EnterpriseIQ AI.

Generate 2-4 practical recommendations based on
the business analysis and exact calculated metrics.

Original business question:
{state["question"]}

Business analysis:
{state["analysis"]}

Exact calculated metrics:
{state["metrics"]}

Rules:
1. Use the supplied metrics as the source of truth.
2. Do not invent or alter numerical values.
3. Do not claim a cause unless the data supports it.
4. Clearly label possible explanations as hypotheses.
5. Do not claim that an industry benchmark is healthy
   unless a benchmark is explicitly provided.
6. If more information is needed, recommend collecting it.
7. Keep recommendations actionable and concise.
8. Do not repeat the entire business analysis.

Return recommendations only.
"""
    )

    return {"recommendation": response.content}
