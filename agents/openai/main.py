from agents import Agent, Runner
from config import OPENAI_API_KEY
import os

# Set API key in env variable for Agents API
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

agent = Agent(name="Assistant", instructions="You are a helpful assistant")

result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
print(result.final_output)

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.