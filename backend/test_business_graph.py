from app.graph.workflow import business_graph

result = business_graph.invoke({
    "question": "What was our overall business performance?",
    "plan": "",
    "analysis": "",
    "recommendation": "",
    "final_response": "",
    "metrics": {},
})

print("\nPlanner Output:")
print(result["plan"])

print("\nBusiness Analysis:")
print(result["analysis"])

print("\nRecommendations:")
print(result["recommendation"])

print("\nFinal Response:")
print(result["final_response"])

print("\nExact Metrics:")
print(result["metrics"])