from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools import TavilySearchResults
from langgraph.prebuilt import create_react_agent 
from langchain_core.messages import AIMessage, HumanMessage
import os 
from dotenv import load_dotenv, find_dotenv

# Step 1: Setup API key for groq and tavily

# Load .env file
load_dotenv(find_dotenv())

def get_env_var(var_name: str) -> str:
    """
    Loads and returns the specified environment variable.
    Raises a ValueError if the variable is not found.
    """
    value = os.environ.get(var_name)
    if not value:
        raise ValueError(f"Missing {var_name} environment variable")
    #print(f"{var_name} is set.")
    return value

# Fetch API keys using the function
GROQ_API_KEY = get_env_var("GROQ_API_KEY")
TAVILY_API_KEY = get_env_var("TAVILY_API_KEY")
OPENAI_API_KEY = get_env_var("OPENAI_API_KEY")

# Step 2: Setup LLM and Tools
openai_llm = ChatOpenAI(model="gpt-4o-mini")

groq_llm = ChatGroq(model="llama-3.3-70b-versatile")

search_tool = TavilySearchResults(max_results=2)

# step 3: Setup AI Agent with search tool functionality
system_prompt = "Act as an AI chatbot who is smart and friendly"

def response_from_agent(llm_id, query, allow_search, system_prompt, provider):
    
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id)
        
    tool = [TavilySearchResults(max_results=2)] if allow_search else []
        
    agent = create_react_agent(
        model=llm,
        tools=tool,
        prompt=system_prompt
    )

    # Step 5: Run the agent with a sample query
   # query = "show me top 10 today trend on X in pakistan?"

    state = {"messages": query}

    response = agent.invoke(state)

    messages = response.get("messages")

    ai_message = [message.content for message in messages if isinstance(message, AIMessage)]

    return ai_message[-1]