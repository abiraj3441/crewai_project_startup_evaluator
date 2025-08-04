from crewai import Crew
from agents.idea_analyst import idea_analyst
from agents.market_researcher import market_researcher
from agents.technical_feasibility import technical_feasibility
from agents.recommendation_engine import recommendation_engine

crew = Crew(
    agents=[
        idea_analyst,
        market_researcher,
        technical_feasibility,
        recommendation_engine
    ],
    verbose=True
)