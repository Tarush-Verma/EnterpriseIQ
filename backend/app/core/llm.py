from langchain_google_genai import ChatGoogleGenerativeAI
from core.config import MODEL_NAME

model = ChatGoogleGenerativeAI(
    model=MODEL_NAME
)