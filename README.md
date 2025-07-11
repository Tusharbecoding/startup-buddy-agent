# Startup Buddy Agent 🚀

An AI-powered startup idea validator and market researcher that helps entrepreneurs validate their business ideas through comprehensive market analysis, competitor research, and viability assessment.

## Features

- **Market Research**: Analyzes market size, trends, target demographics, and demand indicators
- **Competitor Analysis**: Identifies and evaluates competitors, their strategies, pricing, and market positioning
- **Viability Assessment**: Provides actionable recommendations and risk analysis for your startup idea
- **AI-Powered**: Uses Google Gemini 2.0 Flash for intelligent analysis
- **Automated Reports**: Generates detailed markdown reports with findings and recommendations

## Project Structure

```
startup-buddy-agent/
├── agents.py          # AI agent definitions (market researcher, competitor analyzer, viability assessor)
├── tasks.py           # Task definitions for each analysis phase
├── tools.py           # Search tools configuration
├── crew.py            # Main crew orchestration and execution
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## Setup

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key
- Serper API key (for web search)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Tusharbecoding/startup-buddy-agent
cd startup-buddy-agent
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

### API Keys Setup

- **Gemini API Key**: Get it from [Google AI Studio](https://makersuite.google.com/app/apikey)
- **Serper API Key**: Get it from [Serper.dev](https://serper.dev/)

## Usage

1. Edit the startup idea in `crew.py`:

```python
result = crew.kickoff(inputs={'idea': 'Your startup idea here'})
```

2. Run the analysis:

```bash
python crew.py
```

3. The system will:
   - Research market size, trends, and target audience
   - Analyze competitors and their strategies
   - Assess business viability and provide recommendations
   - Generate a detailed report saved as `business_validation.md`

## How It Works

The system uses three specialized AI agents working in sequence:

1. **Market Researcher**: Analyzes market conditions, size, trends, and target demographics
2. **Competitor Analyzer**: Identifies key competitors and analyzes their strategies, pricing, and positioning
3. **Viability Assessor**: Synthesizes findings to provide overall business viability assessment and actionable recommendations

Each agent uses web search capabilities to gather real-time market data and insights.

## Example Output

The system generates a comprehensive markdown report covering:

- Market analysis with size and growth projections
- Target audience demographics and behavior
- Competitive landscape overview
- Business viability assessment
- Risk analysis and mitigation strategies
- Actionable next steps and recommendations

## Configuration

### Agents Configuration

- **Temperature**: 0.5 (balanced creativity and consistency)
- **Memory**: Disabled (for compatibility with Gemini)
- **Tools**: Web search via Serper

### Crew Configuration

- **Process**: Sequential execution
- **Cache**: Enabled for efficiency
- **Max RPM**: 100 requests per minute

## Dependencies

- `crewai`: Multi-agent AI framework
- `crewai-tools`: Additional tools for CrewAI
- `python-dotenv`: Environment variable management
- `google-genai`: Google Gemini AI integration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

**Built with ❤️ using CrewAI and Google Gemini**
