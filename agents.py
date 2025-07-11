from crewai import Agent
from tools import search_tool
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

market_researcher = Agent(
    role="Market Researcher",
    goal="Research market size, trends, and target audience for the business idea: {idea}",
    verbose=True,
    memory=True,
    backstory="You are an expert market analyst with deep knowledge of industry trends and consumer behavior.",
    tools=[search_tool],
    allow_delegation=True,
    llm="gemini/gemini-1.5-flash"
)

competitor_analyzer = Agent(
    role="Competitor Analyzer", 
    goal="Identify and analyze competitors for the business idea: {idea}",
    verbose=True,
    memory=True,
    backstory="You are a competitive intelligence specialist who excels at finding and analyzing business competitors.",
    tools=[search_tool],
    allow_delegation=False,
    llm="gemini/gemini-1.5-flash"
)

viability_assessor = Agent(
    role="Business Viability Assessor",
    goal="Evaluate overall business viability and provide actionable recommendations for: {idea}",
    verbose=True,
    memory=True,
    backstory="You are a seasoned business consultant who helps entrepreneurs validate and improve their business ideas.",
    tools=[search_tool],
    allow_delegation=False,
    llm="gemini/gemini-1.5-flash"
)