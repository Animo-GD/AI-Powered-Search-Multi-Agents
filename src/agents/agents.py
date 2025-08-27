from crewai import Agent
from dotenv import load_dotenv
import os
import sys
import yaml
from tools import scraper_tool,search_engine_tool
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from llm_manager.BasicModel import BasicModel
class agents:
    def __init__(self):
        load_dotenv()
        CONFIG_PATH = os.path.join(os.getcwd(),"config")
        AGENTS_CONFIG_PATH = os.path.join(CONFIG_PATH,"agents.yaml")
        with open(AGENTS_CONFIG_PATH,"r") as f:
            self.agents_conf = yaml.safe_load(f)
        self.mistral = BasicModel().get_mistral()
        self.gptoss = BasicModel().get_gptoss()
        print("role:",self.agents_conf["agent_A"]["role"])
        print("goal:",self.agents_conf["agent_A"]["goal"])
        print("backstory:",self.agents_conf["agent_A"]["backstory"])

    
    
    def agent_A(self):
        return Agent(
            role=self.agents_conf["agent_A"]["role"],
            goal=self.agents_conf["agent_A"]["goal"],
            backstory=self.agents_conf["agent_A"]["backstory"],
            llm=self.gptoss
        )

    def agent_B(self):
        return Agent(
            role=self.agents_conf["agent_B"]["role"],
            goal=self.agents_conf["agent_B"]["goal"],
            backstory=self.agents_conf["agent_B"]["backstory"],
            llm=self.mistral,
            tools=[search_engine_tool]
        )

    def agent_C(self):
        return Agent(
            role=self.agents_conf["agent_C"]["role"],
            goal=self.agents_conf["agent_C"]["goal"],
            backstory=self.agents_conf["agent_C"]["backstory"],
            llm=self.mistral,
            tools=[scraper_tool]
        )

    def agent_D(self):
        return Agent(
            role=self.agents_conf["agent_C"]["role"],
            goal=self.agents_conf["agent_C"]["goal"],
            backstory=self.agents_conf["agent_C"]["backstory"],
            llm=self.gptoss
        )
    
