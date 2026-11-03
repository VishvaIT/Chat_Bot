
import streamlit as st
import requests

from main import chat_stream, check_ollama, MODEL

st.set_page_config(
    page_title="Llama AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CSS ----------------

st.markdown("""
<style>
.stApp {
    background: #0b1020;
    color: #f8fafc;
}

#MainMenu, footer, header {
    visibility: hidden;
}

.block-container {
    max-width: 1050px;
    padding-top: 2rem;
}

section[data-testid="stSidebar"] {
    background: #111827;
    border-right: 1px solid #263244;
}

.hero {
    text-align: center;
    padding: 65px 10px 30px;
}

.hero h1 {
    font-size: 48px;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -2px;
}

.gradient {
    background: linear-gradient(90deg,#60a5fa,#a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    color: #94a3b8;
    font-size: 16px;
}

.feature {
    background: #151e30;
    border: 1px solid #29364a;
    padding: 23px;
    border-radius: 16px;
    min-height: 140px;
}

.feature h4 {
    color: #e2e8f0;
}

.feature p {
    color: #94a3b8;
    font-size: 13px;
}

[data-testid="stChatMessage"] {
    background: #151e30;
    border: 1px solid #29364a;
    border-radius: 15px;
    padding: 14px;
}

.stButton button {
    border-radius: 10px;
    min-height: 42px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- SESSION STATE ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "connected" not in st.session_state:
    st.session_state.connected = None


# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.markdown("# 🤖 Llama AI")
    st.caption("Your personal AI assistant")

    st.divider()

    st.markdown("### Model")
    st.code(MODEL)

    if st.button("🔌 Check Ollama Connection",
                 use_container_width=True):

        with st.spinner("Checking Ollama..."):
            st.session_state.connected = check_ollama()

    if st.session_state.connected is True:
        st.success("Model available")

    elif st.session_state.connected is False:
        st.error("Ollama unavailable or model missing")

    else:
        st.info("Not connected yet")

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.caption("Powered by Python + Streamlit + Ollama")


# ---------------- MAIN HEADER ----------------

st.markdown("""
<div class="hero">
    <h1>Meet <span class="gradient">Llama AI</span></h1>
    <p>Your intelligent local AI assistant.</p>
    <p>Private · Local · Powered by Llama 3.2</p>
</div>
""", unsafe_allow_html=True)


# ---------------- WELCOME SCREEN ----------------

if not st.session_state.messages:

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature">
            <h4>💡 Learn</h4>
            <p>Understand programming and technology.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature">
            <h4>💻 Develop</h4>
            <p>Generate code and solve programming errors.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature">
            <h4>🧠 Explore</h4>
            <p>Brainstorm ideas and build projects.</p>
        </div>
        """, unsafe_allow_html=True)


# ---------------- CHAT HISTORY ----------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ---------------- USER INPUT ----------------

user_input = st.chat_input("Message Llama AI...")

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        try:

            # Connect only when user sends a message
            if st.session_state.connected is not True:

                with st.spinner("Connecting to your local AI..."):

                    if not check_ollama():
                        raise ConnectionError(
                            "Ollama is not running or Llama 3.2 is not installed."
                        )

                st.session_state.connected = True

            with st.spinner("Llama is thinking..."):

                answer = st.write_stream(
                    chat_stream(st.session_state.messages)
                )

            if not answer:
                answer = "The model returned an empty response."

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to Ollama. Start Ollama and try again.")

            st.session_state.messages.pop()

        except requests.exceptions.Timeout:
            st.error("Model response timed out. Please try again.")

            st.session_state.messages.pop()

        except Exception as e:
            st.error(f"Error: {e}")

            st.session_state.messages.pop()
