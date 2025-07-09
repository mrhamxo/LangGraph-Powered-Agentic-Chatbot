from typing import List, Optional
from pydantic import BaseModel, Field
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from ai_agent import response_from_agent
import uvicorn
from dotenv import load_dotenv

load_dotenv()

# Step 1: Setup Pydantic Model ---> Schema 
class RequestState(BaseModel):
    model_name: str = Field(..., description="Name of the LLM model", example="llama-3.3-70b-versatile")
    model_provider: str = Field(..., description="Provider of the model", example="Groq")
    system_prompt: str = Field(..., description="system prompt for setting behavior")
    messages: List[str] = Field(..., description="List of messages in the conversation")
    allow_search: bool = Field(..., description="Enable or disable external search tools")
    # temperature: Optional[float] = Field(default=0.7, ge=0.0, le=1.0, description="Optional controls randomness of the model response")
    # metadata: Optional[dict] = Field(default_factory=dict, description="Optional metadata for custom use cases")

# Step 2: Setup AI Agent from Frontend Request
ALLOWED_MODEL_NAMES = [
    "gpt-4o-mini",
    "llama-3.3-70b-versatile",
    "llama3-70b-8192",
    "mistral-saba-24b",
]

app = FastAPI(title="LangGraph AI Agent API", description="API for AI Agent with LLM and search tool functionality", version="1.0.0")

@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API Endpoint to handle chatbot using LangGraph and Search tools.
    It dynamically selects the model specified in the request and processes the messages.
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        raise ValueError(f"Model {request.model_name} is not supported. Supported models: {ALLOWED_MODEL_NAMES}")
    
    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider

    # Create AI Agent with the specified model and tools
    response = response_from_agent(llm_id, query, allow_search, system_prompt, provider)
    return JSONResponse(content={"response": response})

# step 3: Run app & Explore Swagger UI Docs
if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8000)


