from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Choose which LLM engine to use
api_key = os.getenv("OPENAI_API_KEY")
model = LiteLLMModel(model_id="gpt-4o", api_key=api_key)

# Create a code agent
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)
agent.run("Tell me about Microsoft")