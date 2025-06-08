import os
import google.generativeai as genai
from dotenv import load_dotenv

class AIInterviewCoach:
    def __init__(self, api_key):
        load_dotenv()
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

    def generate_question(self): # Generates a single question
        prompt = """Generate one insightful interview question for a candidate applying for a Software Engineer role. The question should assess problem-solving abilities."""
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error generating question: {e}"

    def answer_question(self, question, answer):
        prompt = f"""Evaluate the following candidate answer to an interview question. The question was: "{question}". The answer is: "{answer}". Provide constructive feedback on the answer, focusing on strengths and weaknesses, and suggest improvements. Consider the answer's clarity, completeness, and demonstration of problem-solving skills."""
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error evaluating answer: {e}"