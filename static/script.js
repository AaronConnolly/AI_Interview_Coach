document.addEventListener('DOMContentLoaded', () => {
    const initialForm = document.getElementById('initial-form');
    const interviewContainer = document.getElementById('interview-container');
    const initialFormContainer = document.getElementById('initial-form-container');
    const chatsContainer = document.querySelector('.chats-container');
    const answerForm = document.getElementById('answer-form');
    let currentQuestionIndex = 0;
    let questions = [];

    initialForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const jobRole = document.getElementById('job_role').value;
        const numQuestions = document.getElementById('num_questions').value;

        try {
            const response = await fetch('/', {
                method: 'POST',
                body: new URLSearchParams({ job_role: jobRole, num_questions: numQuestions }),
            });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            questions = data.questions;
            displayQuestion();
            initialFormContainer.style.display = 'none';
            interviewContainer.style.display = 'block';
        } catch (error) {
            console.error('Error starting interview:', error);
            // Handle the error appropriately, perhaps display a message to the user
        }
    });

    const displayQuestion = () => {
        if (currentQuestionIndex < questions.length) {
            const questionDiv = document.createElement('div');
            questionDiv.classList.add('bot-message', 'message');
            questionDiv.innerHTML = `<p>${questions[currentQuestionIndex]}</p>`;
            chatsContainer.appendChild(questionDiv);
        }
    };

    answerForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const answer = document.getElementById('answer').value;
        const question = questions[currentQuestionIndex];

        // Display the user's message before sending to the API
        const userMessageDiv = document.createElement('div');
        userMessageDiv.classList.add('user-message', 'message');
        userMessageDiv.innerHTML = `<p>${answer}</p>`;
        chatsContainer.appendChild(userMessageDiv);

        try {
            const response = await fetch('/get_feedback', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ question, answer }),
            });

            if (response.ok) {
                const data = await response.json();
                const feedbackDiv = document.createElement('div');
                feedbackDiv.classList.add('bot-message', 'message');
                feedbackDiv.innerHTML = `<p>${data.feedback}</p>`;
                chatsContainer.appendChild(feedbackDiv);
                currentQuestionIndex++;
                document.getElementById('answer').value = ''; // Clear the answer field

                // Display the next question IMMEDIATELY after receiving feedback
                if (currentQuestionIndex < questions.length) {
                    displayQuestion();
                } else {
                    //All questions answered. Handle this appropriately (e.g., display a "Thank You" message)
                    alert("Interview complete!")
                }

            } else {
                console.error('Error:', await response.text());
                //Handle error
            }
        } catch (error) {
            console.error("Error submitting answer:", error);
        }
    });
});