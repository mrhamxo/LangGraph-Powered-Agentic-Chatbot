import streamlit as st
import requests
from prompt_library import prompt_library

# Streamlit Page Config
st.set_page_config(page_title="LangGraph Agent UI", layout="wide")
st.title("🤖 AI Chatbot Agents")
st.write("Create and Interact with AI Agents (Groq / OpenAI)")

# Model Options
MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "llama3-70b-8192", "mistral-saba-24b"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]


# Sidebar: Prebuilt Prompt Selector
st.sidebar.title("🧰 Prompt Library")
selected_template = st.sidebar.selectbox("Choose a predefined agent prompt:", ["None"] + list(prompt_library.keys()))

# Set default values based on template selection
if selected_template != "None":
    st.session_state.system_prompt = prompt_library[selected_template]["system_prompt"]
    default_query = prompt_library[selected_template]["query"]
else:
    default_query = ""

# Session state to preserve config
if "provider" not in st.session_state:
    st.session_state.provider = "Groq"
if "model_name" not in st.session_state:
    st.session_state.model_name = MODEL_NAMES_GROQ[0]
if "system_prompt" not in st.session_state:
    st.session_state.system_prompt = ""
if "allow_search" not in st.session_state:
    st.session_state.allow_search = False

# System Prompt
st.session_state.system_prompt = st.text_area(
    "🧠 Define your AI Agent:",
    value=st.session_state.system_prompt,
    height=70,
    placeholder="Type your agent prompt here..."
)

# Provider Selection
provider = st.radio("🔌 Select Provider:", ("Groq", "OpenAI"))
st.session_state.provider = provider

# Model Selection Based on Provider
if provider == "Groq":
    model_list = MODEL_NAMES_GROQ
else:
    model_list = MODEL_NAMES_OPENAI

st.session_state.model_name = st.selectbox("🎯 Select Model:", model_list)

# Allow Web Search
st.session_state.allow_search = st.checkbox("🌐 Allow Web Search", value=st.session_state.allow_search)

# User Query Input
user_query = st.text_area("💬 Enter your query:", height=150, placeholder="Ask Anything!", value=default_query)

# API Endpoint
API_URL = "http://127.0.0.1:8000/chat"

# Ask Agent Button
if st.button("🚀 Ask Agent!"):
    if not user_query.strip():
        st.warning("❗ Please enter a valid query.")
    else:
        with st.spinner("Talking to the agent..."):
            payload = {
                "model_name": st.session_state.model_name,
                "model_provider": st.session_state.provider,
                "system_prompt": st.session_state.system_prompt,
                "messages": [user_query],
                "allow_search": st.session_state.allow_search
            }

            try:
                response = requests.post(API_URL, json=payload)
                if response.status_code == 200:
                    result = response.json()
                    if "error" in result:
                        st.error("❌ " + result["error"])
                    else:
                        st.subheader("🧠 Agent Response")
                        st.markdown(f"**Final Response:**\n\n{result.get('response', result)}")
                else:
                    st.error(f"⚠️ API returned status code {response.status_code}")
            except Exception as e:
                st.error(f"🔌 Error contacting backend: {e}")
