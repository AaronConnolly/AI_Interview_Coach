from flask import Flask, render_template, request
from interview_coach import AIInterviewCoach
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if api_key is None:
    print("Error: GOOGLE_API_KEY not found in .env file.")
    exit(1)

app = Flask(__name__)
#Tell Flask where to find static files
app.static_folder = 'static'
coach = AIInterviewCoach(api_key=api_key)

question = coach.generate_question()


@app.route("/", methods=["GET", "POST"])
def index():
    feedback = None
    if request.method == "POST":
        answer = request.form.get("answer")
        feedback = coach.answer_question(question, answer)
    return render_template("index.html", question=question, feedback=feedback)

if __name__ == "__main__":
    app.run(debug=True)