from crewai import Crew, Process, LLM
from agents import market_researcher, competitor_analyzer, viability_assessor, llm
from tasks import market_research_task, competitor_analysis_task, viability_assessment_task
import os

if not os.getenv('OPENAI_API_KEY'):
    os.environ['OPENAI_API_KEY'] = 'dummy-key-not-used'

crew = Crew(
    agents=[market_researcher, competitor_analyzer, viability_assessor],
    tasks=[market_research_task, competitor_analysis_task, viability_assessment_task],
    process=Process.sequential,
    memory=False, 
    cache=True,
    max_rpm=100,
    share_crew=True,
    manager_llm=llm
)

result = crew.kickoff(inputs={'idea': 'AI-powered personal fitness coach app'})
print(result)