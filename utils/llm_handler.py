class LLMHandler:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = Config.OPENROUTER_BASE_URL
    
    def get_response(self, prompt, language="English"):
        """Get response from OpenRouter API"""
        if not self.api_key:
            return "⚠️ Please configure OpenRouter API key in Streamlit secrets"
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        system_prompt = f"""You are AgroSage, an expert agricultural assistant for Indian farmers. 
        Respond in {language} language. Provide practical, actionable advice specific to Indian farming conditions.
        Keep responses concise but informative. Include local context and traditional knowledge when relevant."""
        
        payload = {
            "model": Config.MODEL_NAME,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 500,
            "temperature": 0.7
        }
        
        try:
            response = requests.post(self.base_url, headers=headers, json=payload, timeout=30)
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            else:
                return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Connection error: {str(e)}"
