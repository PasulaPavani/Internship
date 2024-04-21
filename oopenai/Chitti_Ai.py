

import streamlit as st
import google.generativeai as genai

# Title styling

# Title and subtitle
st.title('🤖Hello I am  Chitti-The Robot - Your Data Science Assistant')
st.markdown("### :computer:")
st.header('Chitti Robot is Ready to Assist You!')

# Load API key from file
with open(r"C:\Users\LENOVO\Downloads\.gemini_1.5_key.txt") as f:
    api_key = f.read()

# Configure GenerativeAI
genai.configure(api_key=api_key)
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    system_instruction="""Hi! I'm Chitti, your AI assistant for Data Science. I'm here to help you. Feel free to ask me anything related to Data Science or for assistance with any coding challenges you're facing. If the question is not related to data science, please note that I may not be able to provide the assistance you need."""
)

# Initialize chat history if not already present
if "memory" not in st.session_state:
    st.session_state["memory"] = []

# Start chat with the AI model
chat = model.start_chat(history=st.session_state["memory"])
st.chat_message("AI Chiti").write("Hi there! 👋 How can I assist you in Data Science ")

for message in chat.history:
    sender = "AI Chitti" if message.role == "model" else message.role
    st.chat_message(sender).write(message.parts[0].text)

user_input = st.chat_input()

if user_input:
    st.chat_message("user👤").write(user_input)
    response = chat.send_message(user_input)
    for bot in response:
        st.chat_message("AI Chitti🤖").write(bot.text)
    st.session_state["memory"] = chat.history