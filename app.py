import streamlit as st
from rag import ask_hr

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="HR Assistant",
    page_icon="💬",
    layout="centered"
)

# ============================================================
# CSS — DARK BACKGROUND + DARK RED ACCENT
# ============================================================

st.markdown("""
<style>

/* App background (DARK) */
.stApp {
    background-color: #0e1117;
}

/* Main container */
.block-container {
    max-width: 850px;
    padding-top: 2rem;
}

/* Title */
h1 {
    text-align: center;
    color: #e5e7eb;
    font-weight: 600;
    margin-bottom: 24px;
}

/* Chat area */
.chat-area {
    display: flex;
    flex-direction: column;
    gap: 14px;
    margin-bottom: 110px; /* space for bottom input */
}

/* User message (RIGHT) */
.user-msg {
    align-self: flex-end;
    background-color: #7f1d1d;   /* dark red */
    color: #f9fafb;
    padding: 12px 16px;
    border-radius: 14px;
    max-width: 70%;
    font-size: 15px;
    line-height: 1.5;
}

/* Bot message (LEFT) */
.bot-msg {
    align-self: flex-start;
    background-color: #111827;   /* dark card */
    color: #d1d5db;              /* soft light text */
    padding: 14px 18px;
    border-radius: 14px;
    max-width: 70%;
    font-size: 15px;
    line-height: 1.6;
    border: 1px solid #1f2937;
}

/* Input bar (FIXED BOTTOM) */
.input-bar {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: 850px;
    max-width: 95%;
    background-color: #020617;
    padding: 10px 12px;
    border-radius: 14px;
    display: flex;
    gap: 10px;
    border: 1px solid #1f2937;
}

/* Input field */
input[type="text"] {
    background-color: transparent;
    color: #e5e7eb;
    border: none;
    outline: none;
    font-size: 15px;
    flex: 1;
}

/* Placeholder */
input::placeholder {
    color: #6b7280;
}

/* Ask button */
button {
    background-color: #7f1d1d !important;
    color: #ffffff !important;
    border-radius: 10px !important;
    font-size: 14px !important;
    height: 38px !important;
    padding: 0 18px !important;
    border: none !important;
}

button:hover {
    background-color: #991b1b !important;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# SESSION STATE (CHAT HISTORY)
# ============================================================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ============================================================
# TITLE
# ============================================================

st.title("HR Assistant")

# ============================================================
# CHAT HISTORY DISPLAY
# ============================================================

st.markdown("<div class='chat-area'>", unsafe_allow_html=True)

for chat in st.session_state.chat_history:
    st.markdown(
        f"<div class='user-msg'>{chat['question']}</div>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<div class='bot-msg'>{chat['answer']}</div>",
        unsafe_allow_html=True
    )

st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# INPUT BAR (BOTTOM, SAFE FORM)
# ============================================================

with st.form("chat_form", clear_on_submit=True):
    st.markdown("<div class='input-bar'>", unsafe_allow_html=True)

    col1, col2 = st.columns([9, 1])

    with col1:
        user_input = st.text_input(
    "HR Question",
    placeholder="Ask an HR question…",
    label_visibility="collapsed"
)

    with col2:
        send = st.form_submit_button("Ask")

    st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# HANDLE SEND
# ============================================================

if send and user_input.strip():
    result = ask_hr(user_input)

    st.session_state.chat_history.append({
        "question": user_input,
        "answer": result["answer"]
    })

    st.rerun()
