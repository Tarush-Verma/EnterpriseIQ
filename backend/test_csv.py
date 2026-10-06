from app.agents.business_analyst import business_analyst_agent


result = business_analyst_agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": """
                Analyze the business data in
                ../datasets/business_data.csv.

                Calculate the overall profit and profit margin
                across all months.

                Give me the main business insight and a recommendation.
                """
            }
        ]
    }
)

print("\nBusiness Insight:")
print(result["structured_response"])

print("\nType:")
print(type(result["structured_response"]))