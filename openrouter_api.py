import requests
import os

def query_openrouter(prompt):
    api_key = os.getenv("OPENROUTER_API_KEY")  # Set your API key in environment or .env file
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",  # You can change model here
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    try:
        result = response.json()
        if 'choices' in result and result['choices']:
            return result['choices'][0]['message']['content']
        elif 'error' in result:
            return f"OpenRouter error: {result['error'].get('message', 'Unknown error')}"
        else:
            return "Error: Unexpected response format from OpenRouter API."
    except Exception as e:
        return f"Exception while parsing response: {str(e)}"
