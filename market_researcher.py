from crewai import Agent

market_researcher = Agent(
    role='Market Researcher',
    goal='Analyze target market, competitors, and trends',
    backstory='Skilled at identifying market gaps and analyzing customer needs.',
    allow_delegation=False,
    verbose=True
)