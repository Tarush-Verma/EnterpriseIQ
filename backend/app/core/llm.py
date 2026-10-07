from langchain_groq import ChatGroq
from app.core.config import MODEL_NAME

model = ChatGroq(
    model=MODEL_NAME
)