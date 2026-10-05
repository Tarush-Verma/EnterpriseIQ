from langchain_google_genai import ChatGoogleGenerativeAI
from app.core.config import MODEL_NAME

model = ChatGoogleGenerativeAI(
    model=MODEL_NAME
)