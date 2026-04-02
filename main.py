import utils.session
import os 
from dotenv import load_dotenv
from crewai import Crew, Process, LLM
from agents import create_agents
from tasks import create_tasks
from datetime import datetime

load_dotenv()

def save_to_markdown(topic, output):
    with open("report.md", "a", encoding="utf-8") as f:
        f.write(f"\n## Query: {topic}\n")
        f.write(f"**Time:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"{str(output)}\n")
        f.write("\n---\n")

def run(topic):
    
    import os

    llm = LLM(
    model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
    api_key = os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
    max_tokens=150,
    temperature=0.5
)
    
    researcher,writer,reviewer = create_agents(llm)
    
    tasks = create_tasks(topic, researcher, writer, reviewer)
    
    crew = Crew(
        agents=[researcher, writer, reviewer],
        tasks = tasks,
        process=Process.sequential,
        verbose = False
    )
    
    result = crew.kickoff()
    
    return result

if __name__ == "__main__":
    topic = input("Enter topic: ")
    output = run(topic)

    save_to_markdown(topic, output)
    print("\nFinal Output:   ")
    print(output)