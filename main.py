import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Groq API Key and Endpoint
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Fetching the API key from .env
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"  # Corrected endpoint

# Your API Headers (ensure you use correct authentication method for Groq)
headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json",
}

# Sample data for the LLM execution
data = {
    "model": "llama-3.3-70b-versatile",  # Specify the model
    "messages": [{"role": "system", "content": "You are a helpful assistant."},
                 {"role": "user", "content": "Generate a Meta ad campaign."}],
    "max_tokens": 500,
    "temperature": 0.7
}

# Function to make API request
def generate_campaign():
    print("Generating Campaign...")
    
    # Make the POST request to Groq API
    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=data)
        
        # Check for a successful request
        if response.status_code == 200:
            print("Campaign data generated successfully!")
            campaign_data = response.json()
            print(json.dumps(campaign_data, indent=4))  # Pretty print the response
            return campaign_data
        else:
            print(f"Error with Groq API: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

if __name__ == "__main__":
    generate_campaign()
