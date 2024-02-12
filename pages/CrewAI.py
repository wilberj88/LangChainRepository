import streamlit as st
from crewai import Agent, Task, Crew, Process
from langchain.chat_models import ChatOpenAI

api_key1 = st.secrets["OPENAI_API_KEY"]

chat_model = ChatOpenAI(openai_api_key=api_key1)

#CREATE THE AGENTS
monitor_agent = Agent(
  role="Collect and augment climate city data in real time by differents sources",
  goal="Report the overall performance of all climate city data",
  backstory="Expert in extact and monitoring real time data from satellites, IoT, APIs and Machine Learning Models",
  verbose=True
)

alarm_reaction_agent = Agent(
  role="Alarm which natural dissaster are probable and how many lifes are in risk with the report of the climate city data",
  goal="Save lifes with on time alarm system to prevent society affectations by natural dissasters",
  backstory="Expert in reaction in emergencies with international standards for each kind of dissasters",
  verbose=True
)

recommender_preventor_agent = Agent(
  role="Recommend which are the better actions to reduce the risk of natural dissasters",
  goal="Reduce the impact of future natural dissasters in lifes, infraestructures and budgets",
  backstory="Expert in bio finances to budget ecosystem improvements ",
  verbose=True
)


#CREATE THE TASKS
task_monitor_city = Task(
  description="Inform all the day what is the probabilities of ocurrency for natural dissasters by analyzing climate real time data of the city",
  agent=monitor_agent
)

task_alarm_reaction_city = Task(
  description="Inform all the day what alarm is on and which not and give steps of better practices for reaction",
  agent=alarm_reaction_agent
)

task_recommender_prevention_city = Task(
  description="Inform all the day what recommendations are better to improve the sustainability of the city and give steps of better practices for prevent climate dissasters",
  agent=recommender_preventor_agent
)


#CREATE THE CREW
city_crew = Crew(
  agents=[monitor_agent, alarm_reaction_agent, recommender_preventor_agent],
  tasks=[task_monitor_city, task_alarm_reaction_city, task_recommender_prevention_city],
  process=Process.sequential,
  verbose=True
)


#INITIATE THE TEAM WORK
output = city_crew.kickoff()

#SHOW THE RESULT
st.write(output)

