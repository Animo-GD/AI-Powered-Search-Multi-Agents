from crewai import Agent
from crewai.tools import tool
from dotenv import load_dotenv
import os
import yaml
from src.tools import scraper_tool,search_engine_tool

class agents:
    def __init__(self,llm):
        load_dotenv()
        CONFIG_PATH = os.path.join(os.getcwd(),"src","config")
        AGENTS_CONFIG_PATH = os.path.join(CONFIG_PATH,"agents.yaml")
        with open(AGENTS_CONFIG_PATH,"r") as f:
            self.agents_conf = yaml.safe_load(f)
        self.llm = llm

    
    
    def agent_A(self):
        return Agent(
            role=self.agents_conf["agent_A"]["role"],
            goal=self.agents_conf["agent_A"]["goal"],
            backstory=self.agents_conf["agent_A"]["backstory"],
            llm=self.llm
        )

    def agent_B(self):
        return Agent(
            role=self.agents_conf["agent_B"]["role"],
            goal=self.agents_conf["agent_B"]["goal"],
            backstory=self.agents_conf["agent_B"]["backstory"],
            llm=self.llm,
            tools=[self.search_engine_tool]
        )

    def agent_C(self):
        return Agent(
            role=self.agents_conf["agent_C"]["role"],
            goal=self.agents_conf["agent_C"]["goal"],
            backstory=self.agents_conf["agent_C"]["backstory"],
            llm=self.llm,
            tools=[self.scraper_tool]
        )

    def agent_D(self):
        return Agent(
            role=self.agents_conf["agent_C"]["role"],
            goal=self.agents_conf["agent_C"]["goal"],
            backstory=self.agents_conf["agent_C"]["backstory"],
            llm=self.llm
        )
    
