from app.core.llm import model
from app.models.business_insight import BusinessInsight

structured_model = model.with_structured_output(BusinessInsight)