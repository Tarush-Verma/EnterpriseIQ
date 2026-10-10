from typing import TypedDict

class BusinessState(TypedDict):
    question: str
    plan: str
    analysis: str
    recommendation: str
    final_response: str
    metrics: dict