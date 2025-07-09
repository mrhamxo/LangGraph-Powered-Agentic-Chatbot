# 🤖 LangGraph-Powered-Agentic-Chatbot

A production-ready, agentic AI chatbot powered by LangGraph, FastAPI, and Streamlit. Easily switch between LLM providers (Groq, OpenAI), enable web search, and interact with dynamic AI agents tailored to your needs — from code explainer to travel planner.

## 🚀 Features

✅ LangGraph-powered intelligent agents  
✅ Multi-provider model selection (Groq, OpenAI)  
✅ Streamlit-based modern chat UI  
✅ Backend built with FastAPI  
✅ Modular prompt library with 1-click agent loading  
✅ Role-based message support
✅ Optional web search toggle  
✅ Error handling and loading spinners  
✅ Clean, extensible code structure  

## 📁 Project Structure

LangAgentUI/
├── app.py                 # Streamlit UI
├── backend.py             # FastAPI backend
├── ai_agent.py            # LLM and tool invocation logic
├── prompt_library.py      # Modular prompt templates
├── requirements.txt       # Python dependencies
└── .env                   # API keys (Groq, OpenAI Tavily)

## 📸 App Screenshots

### 🎯 Main Chat UI (Streamlit)

<img width="1259" height="579" alt="Image" src="https://github.com/user-attachments/assets/82be5d47-9f1a-45b1-9ddf-fdabf709513f" />

<img width="1247" height="485" alt="Image" src="https://github.com/user-attachments/assets/77835588-139f-4240-87de-9cd8e4468e98" />

## 🔧 Requirements

- Python 3.9+
- `pip install -r requirements.txt`

## 🛠 Setup & Run

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
````

### 2️⃣ Set environment variables

Create a `.env` file in root directory:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
OPENAI_API_KEY=your_openai_api_key
```

### 3️⃣ Run Backend (FastAPI)

```bash
uvicorn backend:app --reload
```

> Access Swagger Docs at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 4️⃣ Run Frontend (Streamlit)

```bash
streamlit run app.py
```

## 🧠 Available Agents

| Name                 | Behavior Description                       |
| -------------------- | ------------------------------------------ |
| 🤖 Helpful Assistant | Friendly, concise general-purpose agent    |
| 🔍 Research Agent    | Cites sources & gathers up-to-date data    |
| 🧠 Code Explainer    | Explains code with examples and analogies  |
| 🩺 Medical Advisor   | Gives factual, non-alarming health info    |
| 📚 Book Recommender  | Personalized book suggestions              |
| 🌍 Travel Planner    | Creates budget-friendly travel itineraries |
| 📈 Startup Advisor   | Mentors early-stage founders               |
| 🎨 Creative Writer   | Helps write stories or poems creatively    |

## 📄 License

MIT License. Free to use, customize, and deploy.