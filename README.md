# online-proctoring-system
![image](https://github.com/user-attachments/assets/c951fea1-79c6-4707-b1ec-f065658d074f)
![image](https://github.com/user-attachments/assets/62367b70-b8d5-4113-bbc5-683f923f6be9)
The directory structure:
online_exam_proctor/
├── app1.py
├── templates/
│   ├── student.html
│   ├── admin.html
├── static/
│   └── (css, js, images)
├── violations.json
Online-Proctoring-System
An intelligent and user-friendly web application designed to ensure academic integrity during online exams by integrating real-time proctoring features such as face detection, head pose estimation, and behavior analysis.

🌐 Overview
The Online Exam Proctor is a Flask-based web application built to monitor and evaluate the behavior of candidates during online tests. It uses computer vision technologies to detect suspicious activities (e.g., looking away from the screen) and generates detailed violation logs along with trust and performance scores.

📸 Screenshots
🧪 Exam Interface
Exam Test

The user is greeted with an intuitive quiz start screen. Once started, the system begins monitoring and analyzing behavior in the background.

📊 Result Dashboard
Result Dashboard

Post-exam, each candidate receives:

Exam Status: Pass/Fail with reason (e.g., Cheating)
Trust Score: Based on behavioral violations
Total Score: Based on quiz performance
Violation Logs: Timestamped incidents with duration and evidence (video link)
🔍 Key Features
🎥 Real-time Face Detection using face_recognition
📐 Head Pose Estimation via MediaPipe for attention tracking
🔗 Violation Records with time, duration, and evidence link
🧠 Trust Score Calculation to judge integrity
⏱ Quiz with Timer and Penalties for incorrect answers
🧾 Detailed Result Report for each candidate
🛠 Tech Stack
Frontend: HTML, CSS, JavaScript (Vanilla or React optional)
Backend: Python, Flask
Database: MySQL
CV Libraries: OpenCV, face_recognition, MediaPipe
Deployment: Can be hosted on Heroku, Render, or local servers
🚀 How to Run
Clone this repository:

git clone https://github.com/your-username/online-exam-proctor.git
cd online-exam-proctor
Install the dependencies:

pip install -r requirements.txt
Run the Flask server:

python app.py
Open http://localhost:5000 in your browser.

📌 Future Enhancements
Audio monitoring for verbal cues
Browser activity tracking (tab switch, fullscreen exit)
Admin dashboard for reviewing all candidate records
Multi-language support
🧑‍💻 Author
Arya Shekhar
Second-year ECE (AI) student at IGDTUW
💡 Passionate about building ethical and secure AI solutions

📃 License
This project is licensed under the MIT License - see the LICENSE file for details. 
