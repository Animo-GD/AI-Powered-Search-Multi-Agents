from dotenv import load_dotenv
import os
def env_setup():
    load_dotenv()
    os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
    os.environ["OPENROUTER_API_KEY"]=os.getenv("OPENROUTER_API_KEY")
    os.environ["OPENAI_API_BASE"]=os.getenv("OPENAI_API_BASE")
    os.environ["OPENAI_MODEL_NAME"]=os.getenv("OPENAI_MODEL_NAME")
if __name__ == "__main__":
    env_setup()