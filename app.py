from flask import Flask, render_template, request, jsonify
from interview_coach import AIInterviewCoach
from response_templates import RESPONSE_TEMPLATES

app = Flask(__name__)
app.static_folder = 'static'
coach = AIInterviewCoach()  # Create the AIInterviewCoach instance

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        job_role = request.form["job_role"]
        num_questions = int(request.form["num_questions"])
        questions = coach.generate_questions(job_role, num_questions)
        return jsonify({"questions": questions})
    return render_template("index.html")

@app.route("/get_feedback", methods=["POST"])
def get_feedback():
    data = request.get_json()
    answer = data.get("answer")
    question = data.get("question")
    if question and answer:
        feedback = coach.answer_question(question, answer)
        return jsonify({"feedback": feedback})
    else:
        return jsonify({"error": "Invalid request data"}), 400

if __name__ == "__main__":
    app.run(debug=True)