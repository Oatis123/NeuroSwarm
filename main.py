from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
from agent import request_to_agent, request_to_agent_with_chat_history
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="NeuroSwarm API",
    description="API for NeuroSwarm multi-agent AI system",
    version="1.0.0"
)

# Pydantic models for request/response
class SimpleRequest(BaseModel):
    request: str

class ChatMessage(BaseModel):
    type: str  # "human", "ai", or "system"
    content: str

class ChatHistoryRequest(BaseModel):
    chat_history: List[ChatMessage]

class AgentResponse(BaseModel):
    response: str
    status: str = "success"

# Helper function to convert chat messages to LangChain format
def convert_to_langchain_messages(chat_messages: List[ChatMessage]):
    """Convert API chat messages to LangChain message format"""
    langchain_messages = []
    for msg in chat_messages:
        if msg.type.lower() == "human":
            langchain_messages.append(HumanMessage(content=msg.content))
        elif msg.type.lower() == "ai":
            langchain_messages.append(AIMessage(content=msg.content))
        elif msg.type.lower() == "system":
            langchain_messages.append(SystemMessage(content=msg.content))
        else:
            # Default to HumanMessage if type is not recognized
            langchain_messages.append(HumanMessage(content=msg.content))
    return langchain_messages

@app.get("/")
async def root():
    """Root endpoint providing API information"""
    return {
        "message": "NeuroSwarm API",
        "description": "Multi-agent AI system with Queen orchestrator and specialized workers",
        "endpoints": {
            "/agent/request": "POST - Send a simple request to the agent",
            "/agent/chat": "POST - Send a request with chat history to the agent",
            "/docs": "GET - API documentation"
        }
    }

@app.post("/agent/request", response_model=AgentResponse)
async def agent_request(request_data: SimpleRequest):
    """
    Send a simple request to the NeuroSwarm agent system.
    
    This endpoint processes a single text request through the Queen agent,
    which orchestrates the appropriate worker agents to handle the task.
    """
    try:
        # Call the agent function
        result = request_to_agent(request_data.request)
        
        # Function now returns string directly
        return AgentResponse(
            response=result,
            status="success"
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Error processing request: {str(e)}"
        )

@app.post("/agent/chat", response_model=AgentResponse)
async def agent_chat_history(request_data: ChatHistoryRequest):
    """
    Send a request with chat history to the NeuroSwarm agent system.
    
    This endpoint allows for context-aware conversations by providing
    the full chat history to the Queen agent for processing.
    
    Message types supported:
    - "human" or "user": Messages from the user/human
    - "ai" or "assistant": Messages from the AI system
    - "system": System messages for context or instructions
    
    Note: If an unrecognized message type is provided, it will default to "human" type.
    """
    try:
        # Convert API messages to LangChain format
        langchain_messages = convert_to_langchain_messages(request_data.chat_history)
        
        # Call the agent function with chat history
        result = request_to_agent_with_chat_history(langchain_messages)
        
        # Function now returns string directly
        return AgentResponse(
            response=result,
            status="success"
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing chat request: {str(e)}"
        )

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "NeuroSwarm API"}

if __name__ == "__main__":
    # Run the FastAPI app with uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )