from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel
import yfinance as yf

# Initialize the model with Ollama configuration
model = LiteLLMModel(
    model_id="ollama/llama3.1",
    api_base="http://localhost:11434",  # Local Ollama endpoint
    api_key="none"  # Ollama doesn't require authentication
)

# Define the agent with tools and imports
agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    additional_authorized_imports=["yfinance"],
    model=model
)

# Run the agent (corrected ticker to MSFT for Microsoft)
response = agent.run(
    "Fetch the stock price of Microsoft Inc (NASDAQ: MSFT). Use the YFinance Library."
)

print(response)