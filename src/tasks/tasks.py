from crewai import Task
from agents.agents import agents
from tools import AllExtractedProducts,ResultQueires,AllSearchResults
import yaml
import os
class tasks:
    global no_keywords
    def __init__(self):
        self.Agents = agents()
        CONFIG_PATH = os.path.join(os.getcwd(),"config")
        TASKS_CONFIG_PATH = os.path.join(CONFIG_PATH,"tasks.yaml")
        os.makedirs("data",exist_ok=True)
        with open(TASKS_CONFIG_PATH,"r") as f:
            self.tasks_conf = yaml.safe_load(f)

   
    def task_A(self):
          return Task(
                description=str(self.tasks_conf["task_A"]["description"]),
                expected_output=self.tasks_conf["task_A"]["expected_output"],
                output_file=os.path.join("data","step1.json"),
                output_json=ResultQueires,
                agent=self.Agents.agent_A()
          )
    def task_B(self):
          return Task(
                description=str(self.tasks_conf["task_B"]["description"]),
                expected_output=self.tasks_conf["task_B"]["expected_output"],
                output_file=os.path.join("data","step2.json"),
                output_json=AllSearchResults,
                agent=self.Agents.agent_B()
          )
    def task_C(self):
          return Task(
                description=str(self.tasks_conf["task_C"]["description"]),
                expected_output=self.tasks_conf["task_C"]["expected_output"],
                output_file=os.path.join("data","step3.json"),
                output_json=AllExtractedProducts,
                agent=self.Agents.agent_C()
          )
    def task_D(self):
          return Task(
                description=str(self.tasks_conf["task_D"]["description"]),
                expected_output=self.tasks_conf["task_D"]["expected_output"],
                output_file=os.path.join("data","FinalReport.html"),
                agent=self.Agents.agent_D()
          )