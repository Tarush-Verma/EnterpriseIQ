from app.agents.business_analyst import business_analyst_agent

questions = [
    "What was our overall business performance?",
    "Which month had the highest revenue?",
    "Which month had the lowest profit?",
    "What was our average monthly profit?",
]

for question in questions :
    print("\n" + "=" * 60)
    print(f"Question: {question}")
    print("=" * 60)
    result = business_analyst_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": f"""
                    Analyze the business data in
                    ../datasets/business_data.csv.

                    {question}

                    Give me a concise business answer.
                    """                
                }
            ]
        }
    )

print("\nBusiness Insight:")
print(result["structured_response"])
