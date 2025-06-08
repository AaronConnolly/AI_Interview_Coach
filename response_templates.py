RESPONSE_TEMPLATES = {
    "positive_feedback": [
        "That's an excellent answer! You clearly demonstrated a strong understanding of [skill/concept].",
        "Great job! Your response was well-structured and effectively addressed all aspects of the question.",
        "I'm impressed with your approach.  Your answer shows a high level of expertise in [area].",
    ],
    "needs_improvement": [
        "Your answer is a good start, but it could be improved by [suggestion 1].  You might also consider [suggestion 2].",
        "While your answer touches upon the key points, it lacks depth in [area]. Consider providing more detail or examples.",
        "Your response is understandable, but it could be more concise and focused on the core aspects of the question.",
    ],
    "unclear_answer": [
        "I'm having difficulty understanding your response. Could you please rephrase it or provide more context?",
        "Your answer seems unclear.  Perhaps providing a more structured explanation would help.",
        "Could you elaborate on your answer? I'm not sure I understand the points you're trying to convey.",
    ],
    "answer_question": [
        """Provide constructive feedback on the answer, focusing on strengths and weaknesses, and suggest 
        improvements. Consider the answer's clarity, completeness, and demonstration of relevant skills for the 
        role. this response should be short and concise so that the use will receive valuable information.
        Give the response in html format so that it can be displayed in a web application.
        Use the following format example:
        <h3>Strengths</h3>
        <p>The answer directly addresses the question and mentions a relevant experience.  You demonstrate a basic understanding of debugging using logs.</p>

        <h3>Weaknesses</h3>
        <ul>
        <li>The answer lacks sufficient detail and depth.</li>
        <li>It doesn't explain *how* the logs revealed the root cause.</li>
        <li>It doesn't specify debugging techniques beyond log analysis.</li>
        <li>Crucial details about team communication and the final solution are omitted.</li>
        <li>Informal language ("It was helpful...") is used.</li>
        </ul>

        <h3>Improvements</h3>
        <ul>
        <li><strong>Elaborate on each step</strong> using the <strong>STAR method</strong> (Situation, Task, Action, Result).</li>
        <li>Describe the specific AI assistant, the prompts used, and the differences observed in the logs (with concrete examples).</li>
        <li>Specify the debugging tools used (if any).</li>  
        <li>Detail the steps taken to fix the bug and how the solution was communicated (e.g., pull requests, team meetings).</li>
        <li>Use more specific details and technical language to showcase stronger problem-solving and communication skills.</li>
        </ul>

        <p>For example, instead of saying "It was helpful...", describe the specific log entries, what they indicated, and how that led you to the root cause. By providing more context and detail, you'll be able to showcase your problem-solving abilities more effectively.</p>
        """
    ],
    "generate_question": [
        "The questions should assess problem-solving abilities, communication skills, and relevant "
        "technical knowledge. your question should be relative size to an actual in-person interview and not have "
        "too much information or too many parts"
    ]
    # Add more template categories as needed
}

