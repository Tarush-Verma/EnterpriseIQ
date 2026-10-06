from pydantic import BaseModel, Field

class BusinessInsight(BaseModel):
    insight: str = Field(description="Main business insight")
    profit: float = Field(description="Calculated business profit")
    profit_margin: float = Field(description="Profit margin as a percentage")
    recommendation: str = Field(description="Business recommendation")