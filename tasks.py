from crewai import Task
from tools import search_tool
from agents import market_researcher, competitor_analyzer, viability_assessor

market_research_task = Task(
    description="Research the market for business idea: {idea}. Find market size, growth trends, target demographics, and demand indicators.",
    expected_output="A comprehensive market analysis report covering market size, trends, target audience, and growth potential.",
    tools=[search_tool],
    agent=market_researcher
)

competitor_analysis_task = Task(
    description="Identify and analyze competitors for business idea: {idea}. Research their strategies, pricing, strengths, and weaknesses.",
    expected_output="A detailed competitor analysis with key players, their positioning, and competitive landscape overview.",
    tools=[search_tool],
    agent=competitor_analyzer
)

viability_assessment_task = Task(
    description="Based on market research and competitor analysis, evaluate the viability of business idea: {idea}. Provide recommendations and next steps.",
    expected_output="A business viability assessment with pros/cons, risk analysis, recommendations, and actionable next steps.",
    tools=[search_tool],
    agent=viability_assessor,
    output_file='business_validation.md'
)