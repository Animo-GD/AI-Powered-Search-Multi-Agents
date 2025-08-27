import os
from crewai import Crew,Process
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agents.agents import agents
from tasks.tasks import tasks
from llm_manager.BasicModel import BasicModel




test1_crew = Crew(
    agents=[agents().agent_A(),agents().agent_B()],
    tasks=[tasks().task_A(),tasks().task_B()],
    process=Process.sequential
)

input_values = {
        "company_name":"Moaaz",
        "product_name":"Coffee machine for office",
        "web_sites":["amazon.com","jumia.com","noon.com"],
        "no_keywords":5,
        "country_name":"Egypt",
        "score_th":0.30,
        "language":"English",
        "top_recommendations_no":10
    }
result = test1_crew.kickoff(
    inputs=input_values
)

