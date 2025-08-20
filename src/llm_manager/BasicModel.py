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
        self.model1=os.getenv("OPENAI_MODEL_NAME")
        self.base_url=os.getenv("OPENAI_API_BASE")
        self.api_key=os.getenv("OPENAI_API_KEY")
        self.model2 = "openai/gpt-oss-20b:free"
        self._llm = LLM(
            model=self.model1,
            base_url=self.base_url,
            api_key=self.api_key,
        )
        self._llm_gptoss = LLM(
            model=self.model2,
            base_url=self.base_url,
            api_key=self.api_key,
        )

    def get_llm(self):
        return self._llm
    def get_free_llm(self):
        return self._llm_gptoss
