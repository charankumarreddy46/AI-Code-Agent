from langchain_groq import ChatGroq

from config import Config


def get_llm():
    """
    Creates and returns the Large Language Model.
    """

    llm = ChatGroq(
        api_key=Config.GROQ_API_KEY,
        model=Config.MODEL_NAME,
        temperature=Config.TEMPERATURE,
    )

    return llm