from app.agents.business_analyst import business_analyst_agent

result = business_analyst_agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": """
                Our company generated revenue of 1,000,000
                with expenses of 700,000.

                What is our profit and profit margin?
                """                
            }
        ]
    }
)

print(result["messages"][-1].content)