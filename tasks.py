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
    description="""Based on market research and competitor analysis, evaluate the viability of business idea: {idea}. 
    
    Structure your response as a professional business report with the following sections:
    1. Executive Summary
    2. Market Opportunity Analysis  
    3. Competitive Landscape Assessment
    4. SWOT Analysis (Strengths, Weaknesses, Opportunities, Threats)
    5. Risk Assessment & Mitigation
    6. Financial Viability Overview
    7. Recommendations & Strategic Direction
    8. Implementation Roadmap (Next Steps)
    
    Use proper markdown formatting with:
    - Clear heading hierarchy (# ## ###)
    - Bullet points with proper spacing
    - Bold text for emphasis
    - Tables where appropriate
    - No code blocks or backticks around the content
    - Professional business language""",
    expected_output="""A comprehensive business viability assessment report in clean markdown format with:
    - Professional document structure
    - Clear section headings and subheadings
    - Well-formatted lists and bullet points
    - Strategic insights and actionable recommendations
    - Implementation timeline and next steps
    - No markdown code blocks or formatting artifacts""",
    tools=[search_tool],
    agent=viability_assessor,
    output_file='business_validation.md'
)