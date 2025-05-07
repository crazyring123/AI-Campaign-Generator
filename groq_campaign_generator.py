# groq_campaign_generator.py

import os
import requests
import json
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Correct way to read API key from .env
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

def generate_campaign_json(user_prompt: str) -> dict:
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    system_prompt = """
You are a professional digital marketing assistant.

Given a campaign idea, respond **only in strict JSON format**, like this:
{
  "campaign_name": "...",
  "objective": "...",
  "target_audience": {
    "age": "...",
    "gender": "...",
    "location": "...",
    "interest": "..."
  },
  "budget_per_day_usd": ...,
  "duration_days": ...,
  "ad_creative": {
    "headline": "...",
    "body_text": "...",
    "call_to_action": "..."
  }
}

⚠️ DO NOT explain or write anything else. DO NOT include Markdown. Just return raw JSON only.
"""


    data = {
        "model": "llama3-70b-8192",  # Use correct model name
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.5
    }

    try:
        response = requests.post(GROQ_URL, headers=headers, json=data)
        response.raise_for_status()

        # Extract text content from response
        content = response.json()["choices"][0]["message"]["content"]
        print("Raw Groq response:", content)

        # Parse the JSON output from the LLM safely
        return json.loads(content)

    except json.JSONDecodeError:
        print("❌ Failed to parse JSON. Check LLM output.")
        return {}

    except Exception as e:
        print("❌ Error communicating with Groq API:", e)
        return {}
