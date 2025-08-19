from crewai import Agent
from crewai.tools import tool
from scrapegraph_py import Client
from tavily import TavilyClient
from dotenv import load_dotenv
import os
import yaml

class agents:
    def __init__(self):
        load_dotenv()
        CONFIG_PATH = os.path.join(os.getcwd(),"src","config")
        AGENTS_CONFIG_PATH = os.path.join(CONFIG_PATH,"agents.yaml")
        with open(AGENTS_CONFIG_PATH,"r") as f:
            self.agents_conf = yaml.safe_load(f)
        self.tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        self.scraper = Client(api_key=os.getenv("SCRAPE_API_KEY"))

    def agent_A():
        return Agent()

    def agent_B():
        return Agent()

    def agent_C():
        return Agent()

    def agent_D():
        return Agent()
    