import streamlit as st
import requests
from agents import agent_tool

# Set app title
st.title("QnA Using SerpAPI")

# Search bar
question = st.text_input("Enter your question")

# Submit button
if st.button("Submit"):
    if question:
        # Get SerpAPI results
        response = agent_tool(question)

        # Display the generated output below
        st.write(response)
    else:
        st.warning("Please enter a question")
