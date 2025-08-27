from crewai import LLM
import os
from dotenv import load_dotenv
from threading import Lock
class BasicModel:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._instance._init_model()
        return cls._instance

    def _init_model(self):
        load_dotenv()
        
        self._mistral = LLM(
                model="mistralai/mistral-small-3.2-24b-instruct:free",
                base_url="https://openrouter.ai/api/v1",
                api_key=os.getenv("OPENAI_API_KEY"),
                custom_llm_provider="openrouter"
        )

        self._gptoss20b = LLM(
            model="openai/gpt-oss-20b:free",
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0
        )


    def get_mistral(self):
        return self._mistral
    def get_gptoss(self):
        return self._gptoss20b
