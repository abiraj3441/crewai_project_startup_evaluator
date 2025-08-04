from crewai import Agent

idea_analyst = Agent(
    role='Idea Analyst',
    goal='Understand and analyze the core of the startup idea',
    backstory='Expert in startup ideation and innovation frameworks.',
    allow_delegation=False,
    verbose=True
)