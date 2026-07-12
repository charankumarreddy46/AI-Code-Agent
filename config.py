import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    # ========= LLM ==========
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    MODEL_NAME = "openai/gpt-oss-120b"

    TEMPERATURE = 0

    # ========= PROJECT ==========
    PROJECTS_DIR = "projects"

    LOGS_DIR = "logs"

    MAX_RETRIES = 3

    # ========= FEATURES ==========
    ENABLE_REVIEW = True

    ENABLE_DEBUGGER = True