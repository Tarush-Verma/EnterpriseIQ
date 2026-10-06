from app.tools.csv_tools import read_csv,analyze_business_data

result = analyze_business_data.invoke({
    "file_path": "../datasets/business_data.csv"
})

print("\nBusiness Analysis:")
print(result)