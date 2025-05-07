import requests
import json

def generate_campaign(prompt):
    url = "https://api.groq.com/v1/completions"  # Double-check the URL
    
    headers = {
        'Authorization': 'Bearer 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',  # Use your correct API key
        'Content-Type': 'application/json'
    }

    payload = {
        "model": "llama-3.3-70b-versatile",  # Make sure the model is correct
        "prompt": prompt,
        "max_tokens": 500,
        "temperature": 0.7  # Optional, adjusts the level of creativity
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        
        if response.status_code == 200:
            content = response.json()["choices"][0]["message"]["content"]
            try:
                campaign_data = json.loads(content)  # Parse JSON if possible
                return campaign_data
            except (ValueError, KeyError) as e:
                return {"error": f"Error parsing response: {e}"}
        else:
            return {"error": f"API request failed with status code {response.status_code}, response: {response.text}"}

    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {e}"}
