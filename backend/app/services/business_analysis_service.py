
from app.agents.business_analyst import business_analyst_agent
from app.tools.csv_tools import analyze_business_data


def analyze_business_question(question: str) -> dict:
    """Analyze business data and return analysis plus exact metrics."""

    file_path = "../datasets/business_data.csv"

    # 1. Calculate metrics using our deterministic tool
    metrics = analyze_business_data.invoke({
        "file_path": file_path
    })

    # 2. Ask the Business Analyst agent to analyze the metrics
    result = business_analyst_agent.invoke({
        "messages": [{
            "role": "user",
            "content": f"""
Analyze the business data in {file_path}.

Exact calculated metrics:
{metrics}

Question:
{question}

Provide a concise, evidence-based business analysis.
Distinguish facts from hypotheses.
Do not invent benchmarks or causes.
Do not generate recommendations; a separate graph
node will handle recommendations.
"""
        }]
    })

    business_analysis = result["messages"][-1].content

    # 3. Return analysis and metrics to the caller
    return {
        "metrics": metrics,
        "analysis": business_analysis,
    }
