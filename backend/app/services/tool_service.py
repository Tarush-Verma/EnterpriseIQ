from app.core.llm import model
from app.tools.business_tools import calculate_profit, calculate_roi

def get_model_with_tools():
    return model.bind_tools([
        calculate_profit,
        calculate_roi
    ])