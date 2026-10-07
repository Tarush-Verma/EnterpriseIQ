from app.services.business_analysis_service import analyze_business_question


result = analyze_business_question(
    "What was our overall business performance?"
)

print("\nBusiness Analysis:")
print(result["analysis"])

print("\nStructured Business Insight:")
print(result["structured_response"])

print("\nType:")
print(type(result["structured_response"]))