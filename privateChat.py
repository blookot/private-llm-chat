import ollama
import streamlit as st

st.set_page_config(page_title="Chatbot Local", page_icon="🤖")
st.title("🤖 Chatbot Local")

# Select model
selected_model = st.sidebar.selectbox(
    "Choisir le modèle",
    ["gemma4:latest", "qwen3:latest", "mistral:latest", "llama3.2:latest"],
    index=0,
)

# Custom instructions
system_prompt = st.sidebar.text_area(
    "Instructions système",
    value="Tu es un assistant conversationnel qui répond *en français uniquement* de manière factuelle, concise et directe.",
    height=150,
)

# Memory init
if "messages" not in st.session_state:
    st.session_state.messages = []

# Reset button
if st.sidebar.button("Effacer la conversation"):
    st.session_state.messages = []
    st.rerun()

# History display
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Pose ta question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Préparation du contexte : Instruction système + Historique de discussion
    full_payload = [{"role": "system", "content": system_prompt}] + st.session_state.messages

    with st.chat_message("assistant"):

        def response_generator():
            stream = ollama.chat(
                model=selected_model,
                messages=full_payload,
                stream=True,
            )
            for chunk in stream:
                yield chunk["message"]["content"]

        full_response = st.write_stream(response_generator())

    st.session_state.messages.append(
        {"role": "assistant", "content": full_response}
    )