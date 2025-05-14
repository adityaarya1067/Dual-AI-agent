import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.messages import HumanMessage
from rich.console import Console
from langchain_core.tools import ToolException

# Load environment variables
load_dotenv()

# Initialize Rich console
console = Console()

# Ensure API keys are set
groq_api_key = os.getenv("GROQ_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY is not set. Check your .env file.")
if not tavily_api_key:
    raise ValueError("TAVILY_API_KEY is not set. Check your .env file.")

# Initialize LLM with proper parameters
llm = ChatGroq(
    api_key=groq_api_key, 
    model="llama3-8b-8192",
    temperature=0.7,
    max_tokens=1024
)

def handle_tool_error(error: ToolException) -> str:
    console.print(f"[bold red]Tool execution failed:[/bold red] {error.args[0]}")
    return f"Tool execution failed: {error.args[0]}"

# Initialize Tavily Search tool
tavily = TavilySearchResults(
    api_key=tavily_api_key, 
    max_results=3,
    k=3  # Explicitly set number of results
)
tavily.handle_tool_error = handle_tool_error

# Use langchain's create_react_agent instead of langgraph's
# Define the prompt template for ReAct
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. You have access to the following tools:\n{tools}\n\nUse the following format:\n\nQuestion: the input question you must answer\nThought: you should always think about what to do\nAction: the action to take, should be one of [{tool_names}]\nAction Input: the input to the action\nObservation: the result of the action\n... (this Thought/Action/Action Input/Observation can repeat N times)\nThought: I now know the final answer\nFinal Answer: the final answer to the original input question"),
    ("human", "{input}"),
    ("human", "Thought: {agent_scratchpad}")
])

# Create the agent using langchain's implementation
agent = create_react_agent(llm, [tavily], prompt)

# Create the agent executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[tavily],
    verbose=True,
    handle_parsing_errors=True
)

def run_agent(question):
    """Run the agent with proper error handling"""
    try:
        console.print(f"\nProcessing question: {question}", style="yellow")
        # Execute the agent
        response = agent_executor.invoke({"input": question})
        console.print("\nAgent:", style="bold green")
        console.print(response.get("output", "No response generated"), style="black on white")
    except ToolException as e:
        handle_tool_error(e)
    except json.JSONDecodeError as e:
        console.print(f"[bold red]JSON Decode Error:[/bold red] {str(e)}")
    except Exception as e:
        console.print(f"[bold red]Unexpected Error:[/bold red] {type(e).__name__}: {str(e)}")
        # Print traceback for debugging
        import traceback
        console.print(traceback.format_exc(), style="dim red")

# Start chat loop
def main():
    console.print("Welcome to the LangChain Agent with Tavily Search", style="bold green")
    console.print("Type 'quit' to exit", style="bold green")
    
    while True:
        user_question = input("\nUser:\n")
        if user_question.lower() in ["quit", "exit", "bye"]:
            console.print("\nAgent:\nHave a nice day! :wave:\n", style="black on white")
            break
        
        run_agent(user_question)

if __name__ == "__main__":
    main()