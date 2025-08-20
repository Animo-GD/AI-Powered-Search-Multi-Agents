import os
from crewai import Crew,Process
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agents.agents import agents
from tasks.tasks import tasks
from llm_manager.BasicModel import BasicModel




llm1 = BasicModel().get_llm()
llm2 = BasicModel().get_llm()


test1_crew = Crew(
    agents=[agents().agent_A()],
    tasks=[tasks().task_A()],
    process=Process.sequential
)

input_values = {
        "company_name":"Moaaz",
        "product_name":"Coffee machine",
        "web_sites":["amazon.com","jumia.com","noon.com"],
        "no_keywords":5,
        "country_name":"Egypt",
        "language":"English",
        "search_score":0.10,
        "top_recommendations_no":10
    }
test1_crew.kickoff(
    inputs=input_values
)