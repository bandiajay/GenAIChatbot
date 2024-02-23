import streamlit as st
from main import genai_engine
from PIL import Image

# Set title
#st.title("MS-Applied Computer Science Chatbot Project")

# Open the image
image = Image.open('/content/chatbot.png')

# Resize the image
image_resized = image.resize((150, 150))  # Adjust the size as needed

# Create a layout with two columns
col1, col2 = st.columns([2, 5])  # Adjust column ratios as needed

# Display the image in the first column
with col1:
    st.image(image_resized, use_column_width=True)

# Display the title in the second column
with col2:
    st.title("MS-Applied Computer Science Chatbot Project")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.text_input("What is up?"):
    # Display user message in chat message container
    #st.echo()
    #st.markdown(f"user: {prompt}")
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = genai_engine(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
