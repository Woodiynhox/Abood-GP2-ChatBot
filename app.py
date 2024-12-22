from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load the environment variables

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

# Debugging home route
print("Starting Flask app...")

@app.route('/test', methods=['GET'])
def test_chatbot():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Chatbot Test</title>
    </head>
    <body>
        <h1>University Advising Chatbot</h1>
        <form action="/api/chatbot" method="post">
            <label for="message">Enter your question:</label><br>
            <input type="text" id="message" name="message" required><br><br>
            <button type="submit">Send</button>
        </form>
    </body>
    </html>
    '''

@app.route('/', methods=['GET'])
def home():
    print("Debug: Home route was called!")
    return "Flask is running!"

@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    print("Debug: Chatbot route was called!")
    data = request.json
    user_message = data.get("message", "")

    custom_data1 = """
        You are a chatbot for our university advising system. Use this information:

        - Advisors:
        - Dr. Mostafa Ibrahim:
            - Office Hours: Sunday to Wednesday, 10 AM to 2 PM
            - Office Location: Building 5, Room 213
            - TEACHES computer Architecture CS228, Logic Design CS120, and Discrete Structures CS114
            
        - Dr. Mohammed Aljammaz:
            - Office Hours: Monday and Thursday, 12:20 PM to 2 PM
            - Office Location: Building 3, Room 230
            - TEACHES Software Security CS442 and Computer Networks CS330

        - Student:
        - Abdullah Alhagbani:
            - Soon-to-be graduate in Computer Science
            - Contact: Riyadh, Saudi Arabia | +966(54-232-1333) | Abdullah.Alhagbani10@gmail.com
            - LinkedIn: [Abdullah's LinkedIn](https://www.linkedin.com/in/abdullah-alhagbani-b9240b23b/)
            - GPA: 4.17
            - Skills: 
                • Proficient in C++, SQL, and JavaScript
                • Database management and optimization
                • Frontend development using HTML, CSS, JS
                • Project management and problem-solving
            - Achievements:
                • Led Enjaz Club for two years, hosting 12 impactful activities
                • Developed various projects, including CCIS Guide Map and Academic Advising System (in progress)
            - Certifications:
                • Penetration Testing Student (eJPT V2), 2024
                • Basics of Data Analysis and Science, 2022
                • Competitive Programming Training, 2022

        - Mushari Alothman:
            - Computer Science student with experience in Web development
            - Contact: Riyadh, Saudi Arabia | 0567614044 | musharialothman44@gmail.com
            - GitHub: [Mushari's GitHub](https://github.com/mushari44)
            - LinkedIn: [Mushari's LinkedIn](https://www.linkedin.com/in/Mushari-Alothman)
            - Skills:
                • Client Side: JavaScript, CSS, HTML, Java, React, Python, Tailwind CSS
                • Server Side: MongoDB, MySQL, Express.js, Node.js, Socket.IO
                • Development: Git, GitHub, OOP, Debugging
            - Achievements:
                • Vice Leader of Competitive Programming Team in Enjaz IMSIU
                • Solved more than 400 problems in competitive programming
                • Ranked 7th on "CoderHub," an Arab platform for programming challenges
                • Achieved 3rd place in IMSIU programming hackathon (prize over 20k SAR)
            - Projects:
                • Academic Advising System (Graduation project in progress)
                • Full-stack online store with React.js, Node.js, Express.js, and MongoDB
                • Robot game for improving understanding of class "enum"
            - Languages: Advanced English
    """


    


    print("Debug: OpenAI API call")

    print("Debug: OpenAI API call")

    try:
        print("Updated custom_data being sent to OpenAI:")
        print(custom_data1)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a university advising chatbot. "
                        "Use the provided information strictly to answer the user's question. "
                        "Prioritize accuracy and only respond based on the given details."
                    ),
                },
                {"role": "assistant", "content": custom_data1},
                {"role": "user", "content": user_message},
            ],
            max_tokens=500,
        )
        reply = response['choices'][0]['message']['content']
        print(f"Chatbot Reply: {reply}")
        return jsonify({"reply": reply})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to fetch chatbot response"}), 500


if __name__ == "__main__":
 print("Starting Flask server...")
 app.run(debug=True)
