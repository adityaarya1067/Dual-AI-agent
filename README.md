# 🚀 AI-Powered Interactive Chatbot

## 🌟 **Overview**
This project is an **AI-driven chatbot** that leverages **LangChain**, **Groq's LLM**, and **Tavily Search API** to provide dynamic and intelligent responses. It follows the **ReAct (Reasoning + Acting) approach**, allowing the chatbot to determine when to respond with its own knowledge or when to fetch real-time information using external tools like web search.

---

## 🔥 **Key Features**

### 🤖 **Conversational AI with Groq LLM**
- Utilizes **Groq’s powerful language model** (`mixtral-8x7b-32768`) for intelligent and context-aware responses.
- Handles **general knowledge questions** without needing external search.

### 🌍 **Real-time Web Search with Tavily API**
- If the chatbot lacks certain information, it automatically queries the **Tavily Search API**.
- Fetches **top 3 search results** for the user’s query to provide accurate, up-to-date information.

### 🛠️ **Advanced Error Handling & Debugging**
- **Detects missing API keys** and **API failures** to prevent crashes.
- Handles **JSON decoding errors** and **tool execution failures** gracefully.
- Uses **Rich Library** for beautifully formatted debugging output.

### ⚡ **Streaming Responses for Real-time Interaction**
- Uses `langgraph.prebuilt.create_react_agent()` to **process responses in chunks**.
- Provides **step-by-step insights** into whether the chatbot is answering directly or using external tools.

### 💬 **Interactive Chat Loop**
- Allows users to continuously chat **until they type** `"quit"`.
- Dynamically **processes** user input and determines the best response strategy.

---

## 🛠️ **Tech Stack & Components**

| **Technology** | **Purpose** |
|--------------|------------|
| **LangChain** | Manages chatbot logic & tool integrations |
| **Groq LLM** | Provides AI-powered conversational responses |
| **Tavily Search API** | Fetches real-time web search results when needed |
| **LangGraph** | Implements **ReAct agent framework** for decision-making |
| **Rich Console** | Enhances debugging and CLI output with rich formatting |
| **dotenv** | Loads **environment variables (API keys)** securely |

---

## ⚙️ **How It Works**

### 🏁 **1️⃣ User Asks a Question**
- The chatbot receives a user query via **terminal input**.

### 🧠 **2️⃣ AI Decides: Answer Directly or Search the Web?**
- If **Groq LLM has enough knowledge**, it responds immediately.
- If additional **real-time information** is needed, it **calls the Tavily Search API**.

### 🔍 **3️⃣ Processing Tool Calls**
- When Tavily is invoked, the bot prints:
  ```bash
  The agent is calling the tool [TavilySearchResults] with the query [Your Query]. Please wait...
  ```
- It retrieves **top 3 relevant search results**.

### ⚡ **4️⃣ Streaming Responses**
- The chatbot **updates responses in real time**, ensuring a seamless user experience.

### 🛑 **5️⃣ Error Handling & Debugging**
- If an API request fails, **clear error messages** are shown.
- If JSON parsing fails, the exact issue is logged for **debugging**.

### 🔁 **6️⃣ Repeat Until Exit**
- Users can continue chatting **until they type** `"quit"` to exit.

---

## 🎯 **Example Chat Flow**

### 🔹 **Case 1: Simple Query (LLM Response)**
```bash
User: Who is the CEO of OpenAI?
Agent:
Sam Altman is the CEO of OpenAI.
```
(No need for a web search; the LLM has the answer.)

### 🔹 **Case 2: Query Requiring a Web Search**
```bash
User: Latest news about Ronaldo?
The agent is calling the tool [TavilySearchResults] with the query [Ronaldo]. Please wait...
Agent:
According to recent news, Cristiano Ronaldo has scored a hat-trick in the latest match...
```
(The chatbot detects that real-time news is needed and fetches it from Tavily Search API.)

---

## 🖼️ **Screenshots**

![Screenshot 1](https://github.com/user-attachments/assets/26a0a84d-8e34-4e33-bde5-db1ddba7138f)
![Screenshot 2](https://github.com/user-attachments/assets/ad6507b2-8c1d-49da-b0f3-02675dee7e7b)
![Screenshot 3](https://github.com/user-attachments/assets/01eeaaf1-2442-4a37-b01a-cbf436092fba)

---

## 🚀 **Future Enhancements**
✅ **Integrate More APIs**: Add weather, stock market, and Wikipedia tools.
✅ **Web-Based UI**: Build a **React.js frontend** with **FastAPI backend**.
✅ **Improved Query Processing**: Use **NLP-based classification** to refine responses.

---

## 📜 **Installation & Setup**
### **Prerequisites**
- Python 3.8+
- API keys for **Groq LLM** and **Tavily Search API**

### **Setup**
```bash
# Clone the repository
git clone https://github.com/your-repo/chatbot-project.git
cd chatbot-project

# Install dependencies
pip install -r requirements.txt

# Create a .env file and add your API keys
nano .env
# Add the following lines:
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key

# Run the chatbot
python chatbot.py
```

---

## 🤝 **Contributing**
Contributions are welcome! Feel free to **fork the repo**, submit **pull requests**, or open **issues**.

---

💡 *Built with passion and AI!* 🚀
