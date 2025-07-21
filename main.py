import streamlit as st
from difflib import get_close_matches

# --- Predefined FAQ data ---
PREDEFINED_QA = {
    "What does the eligibility verification agent (EVA) do?":
        "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections.",

    "What does the claims processing agent (CAM) do?":
        "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements.",

    "How does the payment posting agent (PHIL) work?":
        "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden.",

    "Tell me about Thoughtful AI's Agents.":
        "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others.",

    "What are the benefits of using Thoughtful AI's agents?":
        "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
}

# --- Matching logic ---
def get_best_response(user_input):
    if not user_input or not isinstance(user_input, str):
        return "🤔 Please enter a valid question."

    questions = list(PREDEFINED_QA.keys())
    # Lowercase matching for flexibility
    lower_q = [q.lower() for q in questions]
    match = get_close_matches(user_input.lower(), lower_q, n=1, cutoff=0.6)

    if match:
        original = next(q for q in questions if q.lower() == match[0])
        return PREDEFINED_QA[original]
    else:
        return ("I'm not sure about that yet, but I’m always learning! "
                "You can reach out to support@thoughtful.ai for help.")

# --- Streamlit UI ---
st.set_page_config(page_title="Thoughtful AI Support", page_icon="🤖")
st.title("🤖 Thoughtful AI Support Agent")
st.markdown("Ask me anything about Thoughtful AI's agents and services.")

user_query = st.text_input("Your question:")

if user_query is not None:
    response = get_best_response(user_query)
    st.markdown(f"**Answer:** {response}")
