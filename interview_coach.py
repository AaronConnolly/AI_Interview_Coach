import requests
import json

class AIInterviewCoach:
    def __init__(self, role_description, api_key, api_endpoint):
        self.role_description = role_description
        self.api_key = api_key
        self.api_endpoint = api_endpoint
        self.questions = []

    def generate_questions(self, num_questions=5):
        pass
        

    def answer_question(self, question, answer):
        pass

    def _gemini_api_call(self, prompt):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {"prompt": prompt}  # Simplified data
        try:
            response = requests.post(self.api_endpoint, headers=headers, data=json.dumps(data))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error calling Gemini API: {e}")
            return None