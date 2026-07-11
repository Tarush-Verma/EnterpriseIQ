from langchain_core.messages import SystemMessage, HumanMessage 
from core.llm import model
from prompts.system_prompt import SYSTEM_PROMPT
def run_chat():
    print("=" * 40)
    print("      EnterpriseIQ AI")
    print("=" * 40)
    print("Type 'exit' to quit.\n")

    messages = [
        SystemMessage(
                content=SYSTEM_PROMPT
        )
    ]

    while True:
        question = input("You: ").strip()
        if question.lower() == "exit":
            print("goodbye!")
            break

        messages.append(
            HumanMessage(content = question)
        )
        response = model.invoke(messages)
        print(f"\nAI: {response.content}\n")
        messages.append(response)