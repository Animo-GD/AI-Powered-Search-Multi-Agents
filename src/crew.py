from agents.agents import agents
from tasks.tasks import tasks
from crewai import Process,Crew
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

class crew:
    def __init__(self,about_company:str):
        self.company_context = StringKnowledgeSource(content=about_company)
        Agents = agents()
        Tasks = tasks()
        self.agents = [
            Agents.agent_A(),
            Agents.agent_B(),
            Agents.agent_C(),
            Agents.agent_D()
            ]
        self.tasks = [
            Tasks.task_A(),
            Tasks.task_B(),
            Tasks.task_C(),
            Tasks.task_D()
        ]

    def load_crew(self):
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            knowledge_sources=[self.company_context]
        )
    
    def start_crew(self,input_params:dict):
        return self.load_crew().kickoff(
            inputs=input_params
        )

    