from app.core.structured_model import structured_model

response = structured_model.invoke(
    """
    The company generated revenue of 1,000,000 and
    had expenses of 700,000.

    Analyze the business performance and provide
    the profit, profit margin, main insight,
    and a recommendation.
    """   
)

print(response)
print(type(response))