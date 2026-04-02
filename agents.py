from crewai import Agent

from tools import serper_search_tool 

def create_agents(llm):
    
    researcher = Agent(
        role = "Researcher",
        goal = "find the accurate information about the topic, briefly",
        backstory = "Expert Researcher who gives proper and acurate informations",
        tools = [serper_search_tool],
        llm = llm,
        verbose = True
    )
    
    writer = Agent(
        role = "Writer",
        goal = "Draft a conise explanation and exact information in 3 points",
        backstory = "breaking down complex idea into easy information",
        llm = llm,
        verbose = False
    )
    
    reviewer = Agent(
    role="Reviewer",
    goal="Verify accuracy and ensure output is exactly 5 clean bullet points",
    backstory="A strict fact-checker who validates information and ensures clarity and correctness",
    llm=llm,
    verbose=False
)
    
    return researcher, writer, reviewer