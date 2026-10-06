from app.agents.business_analyst import business_analyst_agent

result = business_analyst_agent.invoke(
    {
        "messages": [{
                "role": "user",
                "content": """
                    Our company generated revenue of 1,000,000
                    and had expenses of 700,000.

                    Analyze our financial performance.
                """
            }
        ]
    }
)

print("\nStructured Business Insight:")
print(result["structured_response"])

print("\nType:")
print(type(result["structured_response"]))