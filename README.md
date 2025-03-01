This project is an interactive AI-powered chatbot that integrates LangChain, Groq's LLM, and Tavily Search API to answer user queries dynamically. It follows a ReAct (Reasoning + Acting) approach, meaning it can decide when to call external tools (like web search) and when to respond directly.

Key Features
Conversational AI with Groq LLM

Uses Groq’s large language model (mixtral-8x7b-32768) for intelligent responses.
Handles general user queries without needing external search.
Real-time Web Search with Tavily API

If the chatbot lacks information, it calls Tavily Search API to fetch relevant results.
Returns the top 3 search results based on the query.
Error Handling & Debugging Support

Detects API failures or missing keys and provides informative messages.
Handles JSON decoding errors, tool failures, and unexpected issues gracefully.
Uses Rich Library for enhanced debugging output.
Streamed Responses for Real-time Interaction

Uses langgraph.prebuilt.create_react_agent() to process responses in chunks.
Prints intermediate steps, including when the chatbot decides to use external tools.
Interactive Chat Loop

Allows users to continuously chat until they type "quit".
Dynamically processes user messages and determines the best response.
Tech Stack & Components
Technology	Purpose
LangChain	Manages the chatbot logic & tool integrations.
Groq LLM	Provides AI-powered conversational responses.
Tavily Search API	Fetches real-time web search results when needed.
LangGraph	Implements ReAct agent framework for reasoning + tool use.
Rich Console	Formats output beautifully in the terminal.
dotenv	Loads environment variables (API keys).
How It Works
1️⃣ User Asks a Question
The chatbot receives a user query through the terminal.
2️⃣ AI Decides: Answer Directly or Search the Web?
If the Groq LLM has enough information, it responds directly.
If external knowledge is needed, the AI calls the Tavily Search API.
3️⃣ Processing Tool Calls
If Tavily is used, the bot prints:
scss
Copy
Edit
The agent is calling the tool [TavilySearchResults] with the query [Your Query]. Please wait...
It retrieves the top 3 search results.
4️⃣ Streaming Responses
The chatbot continuously updates responses in real time.
5️⃣ Error Handling & Debugging
If an API request fails, a user-friendly error message is shown.
If JSON parsing fails, it logs the exact issue.
6️⃣ Repeat Until Exit
The user can ask multiple queries in a loop until they type "quit".
Example:
![Screenshot 2025-03-01 210539](https://github.com/user-attachments/assets/26a0a84d-8e34-4e33-bde5-db1ddba7138f)
![Screenshot 2025-03-01 210531](https://github.com/user-attachments/assets/ad6507b2-8c1d-49da-b0f3-02675dee7e7b)
![Screenshot 2025-03-01 210520](https://github.com/user-attachments/assets/01eeaaf1-2442-4a37-b01a-cbf436092fba)
