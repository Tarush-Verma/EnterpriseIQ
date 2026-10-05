from app.services.tool_service import get_model_with_tools
from app.tools.business_tools import calculate_profit, calculate_roi
from langchain_core.messages import HumanMessage, ToolMessage

model_with_tools = get_model_with_tools()

messages = [
    HumanMessage(
        content="The company invested ₹100,000 and got ₹130,000 back. Calculate the ROI."
    )
]

response = model_with_tools.invoke(messages)

messages.append(response)

for tool_call in response.tool_calls:
    if tool_call["name"] == "calculate_profit":
        result = calculate_profit.invoke(tool_call["args"])

    elif tool_call["name"] == "calculate_roi":
        result = calculate_roi.invoke(tool_call["args"])

    else:
        raise ValueError(f"Unknown tool: {tool_call['name']}")

    messages.append(
        ToolMessage(
            content=str(result),
            tool_call_id=tool_call["id"]
        )
    )

final_response = model_with_tools.invoke(messages)

print("\n Final answer:")
print(final_response.content)

