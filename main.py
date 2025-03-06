import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
from rich.console import Console
from langchain_core.tools import ToolException

# Load environment variables
load_dotenv()

# Initialize Rich console
rich = Console()

# Ensure API keys are set
groq_api_key = os.getenv("GROQ_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY is not set. Check your .env file.")
if not tavily_api_key:
    raise ValueError("TAVILY_API_KEY is not set. Check your .env file.")

# Initialize LLM
llm = ChatGroq(api_key=groq_api_key, model="mixtral-8x7b-32768")

def handle_tool_error(error: ToolException) -> str:
    rich.print(f"[bold red]Tool execution failed:[/bold red] {error.args[0]}")
    return f"Tool execution failed: {error.args[0]}"

# Initialize Tavily Search tool
tavily = TavilySearchResults(api_key=tavily_api_key, max_results=3)
tavily.handle_tool_error = handle_tool_error

# Create LangGraph agent
langgraph_agent = create_react_agent(model=llm, tools=[tavily])

def process_chunks(chunk):
    """Processes agent response chunks and handles tool calls."""
    if "agent" in chunk:
        for message in chunk["agent"]["messages"]:
            if "tool_calls" in message.additional_kwargs:
                for tool_call in message.additional_kwargs["tool_calls"]:
                    try:
                        tool_name = tool_call["function"]["name"]
                        tool_arguments = json.loads(tool_call["function"]["arguments"])
                        tool_query = tool_arguments.get("query", "Unknown Query")
                        rich.print(
                            f"\nThe agent is calling the tool [deep_sky_blue1]{tool_name}[/deep_sky_blue1] with query [deep_sky_blue1]{tool_query}[/deep_sky_blue1]...",
                            style="deep_sky_blue1"
                        )
                    except (KeyError, json.JSONDecodeError) as e:
                        rich.print(f"[bold red]Error processing tool call:[/bold red] {str(e)}")
            else:
                rich.print(f"\nAgent:\n{message.content}", style="black on white")

# Start chat loop
while True:
    user_question = input("\nUser:\n")
    if user_question.lower() == "quit":
        rich.print("\nAgent:\nHave a nice day! :wave:\n", style="black on white")
        break
    try:
        for chunk in langgraph_agent.stream({"messages": [HumanMessage(content=user_question)]}):
            process_chunks(chunk)
    except ToolException as e:
        handle_tool_error(e)
    except json.JSONDecodeError as e:
        rich.print(f"[bold red]JSON Decode Error:[/bold red] {str(e)}")
    except Exception as e:
        rich.print(f"[bold red]Unexpected Error:[/bold red] {str(e)}")
