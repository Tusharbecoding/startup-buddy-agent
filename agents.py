from crewai import Agent, LLM
from tools import search_tool
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['GEMINI_API_KEY'] = os.getenv('GEMINI_API_KEY')

# Configure Gemini LLM
llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.5,
)

market_researcher = Agent(
    role="Market Researcher",
    goal="Research market size, trends, and target audience for the business idea: {idea}",
    verbose=True,
    memory=False, 
    backstory="You are an expert market analyst with deep knowledge of industry trends and consumer behavior.",
    tools=[search_tool],
    allow_delegation=True,
    llm=llm
)

competitor_analyzer = Agent(
    role="Competitor Analyzer", 
    goal="Identify and analyze competitors for the business idea: {idea}",
    verbose=True,
    memory=False,  
    backstory="You are a competitive intelligence specialist who excels at finding and analyzing business competitors.",
    tools=[search_tool],
    allow_delegation=False,
    llm=llm
)

viability_assessor = Agent(
    role="Business Viability Assessor",
    goal="Evaluate overall business viability and provide actionable recommendations for: {idea}",
    verbose=True,
    memory=False, 
    backstory="""You are a seasoned business consultant and report writer who helps entrepreneurs validate and improve their business ideas. 
    You excel at creating professional, well-structured business reports using clean markdown formatting. 
    You always use proper heading hierarchy, bullet points, and formatting without code blocks or backticks around content.""",
    tools=[search_tool],
    allow_delegation=False,
    llm=llm
)