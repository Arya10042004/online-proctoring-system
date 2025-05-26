from flask import Flask, render_template, jsonify
from detection.proctor_engine import ProctorEngine

app = Flask(__name__)
engine = ProctorEngine()

@app.route('/')
def home():
    return render_template('student.html')

@app.route('/start-exam')
def start_exam():
    result = engine.start_detection(duration=15)
    return jsonify(result)

@app.route('/admin')
def admin():
    logs = engine.get_violation_logs()
    return render_template('admin.html', logs=logs)

if __name__ == '__main__':
    app.run(debug=True)
