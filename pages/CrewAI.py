import streamlit as st
from crewai import Agent, Task, Crew, Process

#create the agents
monitor_agent = Agent(
  role="",
  goal="",
  backstory="",
  verbose=True
)

alarm_reaction_agent = Agent(
  role="",
  goal="",
  backstory="",
  verbose=True
)

recommender_preventor_agent = Agent(
  role="",
  goal="",
  backstory="",
  verbose=True
)

