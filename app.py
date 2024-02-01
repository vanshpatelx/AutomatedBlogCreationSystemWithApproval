from crewai import Agent, Task, Crew, Process
# from langchain_google_vertexai import VertexAI
from langchain_community.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()
import os
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# llm_vertex = VertexAI(model_name="gemini-pro")
llm_google = ChatGoogleGenerativeAI(model="gemini-pro", temprecture=0.3)
# Create Agents

researcher = Agent(
    role='Senior Researcher',
    goal='Discover groundbreaking technologies',
    backstory='A curious mind fascinated by cutting-edge innovation and the potential to change the world, you possess comprehensive knowledge of technology.',
    verbose=True,
    tools=[search_tool],
    allow_delegation=False,
    llm=llm_google
)

insight_researcher = Agent(
    role='Insight Researcher',
    goal='Discover Key Insights',
    backstory='You excel at extracting key insights from the data provided.',
    verbose=True,
    allow_delegation=False,
    llm=llm_google
)

writer = Agent(
    role='Tech Content Strategist',
    goal='Craft compelling content on tech advancements',
    backstory='Renowned as a content strategist, you specialize in making complex tech topics interesting and easy to understand.',
    verbose=True,
    allow_delegation=False,
    llm=llm_google
)

formater = Agent(
    role='Markdown Formatter',
    goal='Format the text in markdown',
    backstory='Your expertise lies in converting text into markdown format.',
    verbose=True,
    allow_delegation=False,
    llm=llm_google
)

# Tasks

research_task = Task(
    description='Identify the next big trend in AI by searching the internet',
    agent=researcher
)

insights_task = Task(
    description='Identify a few key insights from the data in bullet point format. Do not use any tools.',
    agent=insight_researcher
)

writer_task = Task(
    description='Write a short blog post with subheadings. Do not use any tools.',
    agent=writer
)

format_task = Task(
    description='Convert the text into markdown format. Do not use any tools.',
    agent=formater
)


# Creating the tech_crew

tech_crew = Crew(
    agents=[researcher, insight_researcher, writer, formater],
    tasks=[research_task, insights_task, writer_task, format_task],
    process=Process.sequential  # Tasks will be executed one after the other
)


def main():
    st.set_page_config("Agent")
    st.header("Chat with Personal Agent Team 💁")

    user_question = st.text_input("Tell task to do")

    if user_question:
        result = tech_crew.kickoff()
        print(result)
        st.write(result)
        

if __name__ == "__main__":
    main()