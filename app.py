import streamlit as st
from chatbot import FAQChatbot

st.set_page_config(
    page_title="FAQ Chatbot",
    layout="centered",
    page_icon="💬"
)

# Custom CSS for enhanced UI and animations
st.markdown("""
<style>
/* Animated background gradient */
body, .stApp {
    background: linear-gradient(270deg, #0f0c29, #302b63, #24243e);
    background-size: 600% 600%;
    animation: bgAnim 20s ease infinite;
    color: white;
    font-family: 'Segoe UI', sans-serif;
    overflow-x: hidden;
}
@keyframes bgAnim {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Floating circles */
.floating-circles::before, .floating-circles::after {
    content: '';
    position: fixed;
    width: 150px;
    height: 150px;
    border-radius: 50%;
    background: rgba(0, 255, 229, 0.1);
    animation: float 6s ease-in-out infinite alternate;
    z-index: -1;
}
.floating-circles::after {
    top: 30%;
    left: 70%;
}
.floating-circles::before {
    top: 60%;
    left: 20%;
}
@keyframes float {
    0% {transform: translateY(0px);}
    100% {transform: translateY(-20px);}
}

/* Sexy glowing title */
h1 {
    font-size: 3.5rem;
    text-align: center;
    color: #00ffe5;
    text-shadow: 0 0 15px #00ffe5, 0 0 25px #00ffe5;
    animation: pulseTitle 3s infinite ease-in-out;
}
@keyframes pulseTitle {
    0%, 100% { text-shadow: 0 0 15px #00ffe5; }
    50% { text-shadow: 0 0 30px #00ffe5; }
}

/* Input field */
.stTextInput input {
    background-color: rgba(255, 255, 255, 0.1);
    border: 1px solid #00ffe5;
    border-radius: 12px;
    font-size: 1.2rem;
    color: white;
    padding: 10px;
    box-shadow: 0 0 10px rgba(0, 255, 229, 0.3);
}

/* Glowing hover button */
.stButton>button {
    background: linear-gradient(90deg, #00ffe5, #0077ff);
    border: none;
    padding: 12px 25px;
    font-size: 1.2rem;
    border-radius: 10px;
    color: black;
    font-weight: bold;
    transition: 0.3s ease;
    box-shadow: 0 0 15px rgba(0, 255, 229, 0.3);
}
.stButton>button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #00c2ff, #00ffe5);
    color: white;
    box-shadow: 0 0 30px rgba(0, 255, 229, 0.6);
}

/* Glowy answer box */
.response-box {
    margin-top: 2rem;
    padding: 1.5rem;
    background: rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    font-size: 1.2rem;
    line-height: 1.7;
    border-left: 5px solid #00ffe5;
    box-shadow: 0 0 25px rgba(0, 255, 229, 0.2);
    backdrop-filter: blur(12px);
    animation: fadeIn 1s ease;
}

/* Footer */
.footer {
    margin-top: 4rem;
    text-align: center;
    font-size: 0.9rem;
    color: #ccc;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
""", unsafe_allow_html=True)

# Add floating elements class
st.markdown('<div class="floating-circles"></div>', unsafe_allow_html=True)

# Title
st.markdown("<h1>💬 AI-Powered FAQ Chatbot</h1>", unsafe_allow_html=True)

# Load chatbot
bot = FAQChatbot("faq_dataset.csv")

# Ask user
user_input = st.text_input("Ask your question:")

if st.button("Get Answer"):
    if user_input.strip():
        answer = bot.generate_answer(user_input)
        st.markdown(f"<div class='response-box'><strong>Answer:</strong><br>{answer}</div>", unsafe_allow_html=True)
    else:
        st.warning("Please enter a question.")

# Footer
st.markdown("<div class='footer'>🚀 Built with ❤️ using OpenRouter API + IR + RAG</div>", unsafe_allow_html=True)
