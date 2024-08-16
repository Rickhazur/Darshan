import streamlit as st
import requests

# Directly set the API key
API_KEY = "proj-5M0xU5muIVV_STrj6I9tHAYdwZZvyd748eNFL-2JmYBvumjWgR7IGxtVMiT3BlbkFJZ8o9CnbPlqDhoCOb7mnOy2iTKSM4_6oApVmO2GOs-OW0koqmLpFH7VGJoA"

# Simple Streamlit UI
st.title("API Interaction with Streamlit")

# Input field for a word (or any other input your API requires)
word = st.text_input("Enter a word:")

if st.button("Get Definition"):
    if API_KEY:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        response = requests.post(
            "https://api.example.com/define",  # Replace with the actual API URL
            headers=headers,
            json={"word": word}
        )
        if response.status_code == 200:
            st.write(response.json())
        else:
            st.error("API request failed")
    else:
        st.error("API key is missing!")
