import streamlit as st
import requests

# Directly set the API key (consider using environment variables for security)
API_KEY = "proj-5M0xU5muIVV_STrj6I9tHAYdwZZvyd748eNFL-2JmYBvumjWgR7IGxtVMiT3BlbkFJZ8o9CnbPlqDhoCOb7mnOy2iTKSM4_6oApVmO2GOs-OW0koqmLpFH7VGJoA"  # Replace with your actual API key

# Simple Streamlit UI
st.title("API Interaction with Streamlit")

# Input field for a word (or any other input your API requires)
word = st.text_input("Enter a word:")

if st.button("Get Definition"):
    if API_KEY:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"  # Added missing comma here
        }
        try:
            response = requests.post(
                "https://api.example.com/define",  # Replace with the actual API URL
                headers=headers,
                json={"word": word}
            )
            response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
            st.write(response.json())
        except requests.exceptions.HTTPError as http_err:
            st.error(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError:
            st.error("Failed to connect to the server. Please check your internet connection.")
        except requests.exceptions.Timeout:
            st.error("The request timed out. Please try again later.")
        except requests.exceptions.RequestException as req_err:
            st.error(f"An error occurred: {req_err}")
    else:
        st.error("API key is missing")
