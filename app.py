import streamlit as st
from openai import OpenAI
from utils import create_chat_completion, extract_text_from_pdf

# Must be the first Streamlit command
st.set_page_config(page_title="OpenRouter Chatbot", page_icon="🤖", layout="wide")

# Add custom CSS for a more professional look
st.markdown("""
<style>
    .stChatFloatingInputContainer {
        padding-bottom: 20px;
    }
    .stMarkdown {
        font-family: 'Arial', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state variables
if "api_key" not in st.session_state:
    st.session_state.api_key = ""
if "model" not in st.session_state:
    st.session_state.model = "openai/gpt-3.5-turbo"
if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = None

# Sidebar for settings
with st.sidebar:
    st.title("⚙️ Settings")
    sidebar_api_key = st.text_input("Enter your OpenRouter API key", type="password", key="sidebar_api_key")
    sidebar_model = st.text_input("Enter model name (e.g., openai/gpt-3.5-turbo)", value=st.session_state.model, key="sidebar_model")
    
    if st.button("Submit Settings"):
        st.session_state.api_key = sidebar_api_key
        st.session_state.model = sidebar_model
    
    st.markdown("---")
    
    # PDF upload section
    st.subheader("📄 Upload PDF")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is not None:
        pdf_text = extract_text_from_pdf(uploaded_file)
        if pdf_text:
            st.session_state.pdf_text = pdf_text
            st.success("PDF uploaded successfully!")
        else:
            st.error("Failed to process PDF file")
    
    # Clear buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Clear Chat"):
            st.session_state.messages = []
            st.rerun()
    with col2:
        if st.button("Clear PDF"):
            st.session_state.pdf_text = None
            st.rerun()
        
    st.markdown("---")
    st.markdown("Powered by [OpenRouter](https://openrouter.ai/), built with 💖 by [Faris Faiz](https://www.linkedin.com/in/muhammad-faris-ahmad-faiz-ab9b35212/)")

# Set page title
st.title("🤖 OpenRouter Chatbot")
if st.session_state.pdf_text:
    st.markdown("📄 PDF loaded - Ask questions about the document!")
else:
    st.markdown("Upload a PDF in the sidebar to chat about its contents, or just chat with the AI!")

# Main page API key input if not provided
if not st.session_state.api_key:
    st.warning("Please enter your OpenRouter API key in the sidebar. If you don't have one, get it from [OpenRouter](https://openrouter.ai/)")
    st.stop()

# Initialize the OpenAI client with OpenRouter's base URL
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.session_state.api_key
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Keep only last 2 messages in history
    if len(st.session_state.messages) > 4:  # 4 because each exchange has 2 messages (user + assistant)
        st.session_state.messages = st.session_state.messages[-4:]
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # Get response using create_chat_completion from utils.py
        response = create_chat_completion(
            client,
            [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            st.session_state.model,
            st.session_state.pdf_text
        )
        
        if response:
            message_placeholder.markdown(response)
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})

# Add a footer
st.markdown("---")
st.markdown("Powered by [OpenRouter](https://openrouter.ai/), built with 💖 by [Faris Faiz](https://www.linkedin.com/in/muhammad-faris-ahmad-faiz-ab9b35212/)")
