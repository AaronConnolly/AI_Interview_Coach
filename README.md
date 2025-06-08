# AI Interview Coach (gemini-1.5-flash-latest)

This project is a web application that simulates an interview experience using the Google Gemini AI model.  It helps users practice answering interview questions and receive feedback on their responses.

[![Screenshot 1](image1.png)](image1.png)
[![Screenshot 2](image2.png)](image2.png)


## Features

*   **Interactive Interview Simulation:**  Users can specify the job role and the number of questions they want to practice. The application then dynamically generates interview questions and provides feedback on each answer.

*   **AI-Powered Feedback:** The application uses Google Gemini to assess user answers and provide detailed feedback, including strengths, weaknesses, and suggestions for improvement.

*   **Clear and Concise Feedback:** The AI is prompted to give feedback that is well-structured and easy to understand, using paragraphs, bullet points, and headings.

*   **Multiple Questions:** The application supports multiple interview questions within a single interview session, allowing for comprehensive practice.

*   **Responsive Design:** The application is designed to be responsive and work well across various screen sizes.


## Technologies Used

*   **Frontend:** HTML, CSS, JavaScript
*   **Backend:** Python (Flask), Google Gemini API
*   **Other:**  `dotenv` (for managing environment variables)


## Getting Started

**1. Setting up the Backend:**

*   Create a Google Cloud project and enable the Gemini API.
*   Obtain a Gemini API key and store it securely in a `.env` file (`.env` is added to `.gitignore` so the API key isn't added to the Github repo).
*   Install Python dependencies: `pip install Flask google-generativeai python-dotenv`
*   Run the Flask app: `python app.py` (Ensure the Gemini API is enabled and configured correctly).

**2. Running the Application:**

*   Open your web browser and go to `http://127.0.0.1:5000/` (or the appropriate address where your Flask app is running).

## Future Improvements

**1. Make the UI more user-friendly**
*   Add a scroll-wheel for when the AI is generating a response

**2. Give overrall feedback at the end of the interview and key areas to improve**
*  This would involve storing previous answers and repsonses and ginvind feedback on the entire conversation
