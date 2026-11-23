from langchain_ollama import ChatOllama
from app.config import(
    MODEL_NAME,
    OLLAMA_BASE_URL,
    TEMPERATURE
)
#get_llm() function creates the model instance and returns it.
def get_llm():
    """
    Creates and returns the ollama chat model instance with the specified configuration.
    """
    llm = ChatOllama(
        model=MODEL_NAME,
        base_url=OLLAMA_BASE_URL,
        temperature=TEMPERATURE
    )
    return llm