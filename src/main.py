from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os


def env_setup():
    load_dotenv()
    os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
    os.environ["OPENAI_API_BASE"]=os.getenv("OPENAI_API_BASE")
    os.environ["OPENAI_MODEL_NAME"]=os.getenv("OPENAI_MODEL_NAME")

def load_llm():
    return ChatOpenAI(
        model=os.getenv("OPENAI_MODEL_NAME"),
        base_url=os.getenv("OPENAI_API_BASE"),
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0
    )
if __name__ == "__main__":
    env_setup()
    base_llm = load_llm()
    print(base_llm.invoke(["Once upon a time"]).content)