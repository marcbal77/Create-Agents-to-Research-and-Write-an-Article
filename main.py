# Warning control
import warnings
warnings.filterwarnings('ignore')

from crewai import Agent, Task, Crew, Process
from langchain.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

# Define our agents
researcher = Agent(
    role='Research Analyst',
    goal='Conduct thorough research on given topics and compile relevant information',
    backstory="""You are an expert research analyst with a keen eye for credible information.
    Your specialty is finding and synthesizing information from various sources.""",
    tools=[search_tool],
    verbose=True
)

writer = Agent(
    role='Content Writer',
    goal='Create engaging and informative articles based on research',
    backstory="""You are a skilled content writer with expertise in creating 
    well-structured, engaging articles. You excel at turning complex information 
    into readable content.""",
    verbose=True
)

editor = Agent(
    role='Editor',
    goal='Ensure article quality and accuracy',
    backstory="""You are a meticulous editor with years of experience in 
    content refinement. You ensure articles are polished, accurate, and 
    engaging.""",
    verbose=True
)

# Define the tasks
research_task = Task(
    description="""Research the topic: 'The Future of Artificial Intelligence in Healthcare'
    Focus on recent developments, potential applications, and expert predictions.
    Compile key findings and important statistics.""",
    agent=researcher
)

writing_task = Task(
    description="""Using the research provided, write a comprehensive article about 
    'The Future of Artificial Intelligence in Healthcare'. Structure it with clear 
    sections, include relevant examples, and maintain an engaging tone.""",
    agent=writer
)

editing_task = Task(
    description="""Review and refine the article. Check for clarity, accuracy, 
    flow, and engagement. Ensure all information is well-presented and the article 
    maintains a professional tone.""",
    agent=editor
)

# Create the crew
crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[research_task, writing_task, editing_task],
    verbose=2,
    process=Process.sequential
)

# Execute the tasks
result = crew.kickoff()

# Print the final result
print("\nFinal Article:")
print(result)
