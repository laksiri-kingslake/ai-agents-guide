from smolagents import CodeAgent, DuckDuckGoSearchTool, OpenAIServerModel
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Choose which LLM engine to use
api_key = os.getenv("TOTHER_API_KEY")

# Choose Together based DeepSeek model to use
model = OpenAIServerModel(
    model_id="deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
    api_base="https://api.together.xyz/v1/", # Leave this blank to query OpenAI servers.
    api_key=api_key, # Switch to the API key for the server you're targeting.
)

# Create a code agent
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)
# agent.run("Tell me about Microsoft")
agent.run("Hi")