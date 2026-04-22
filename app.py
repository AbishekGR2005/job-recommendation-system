from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


jobs = pd.DataFrame({
    'job_title': ['Data Analyst', 'Software Engineer', 'Machine Learning Engineer', 'Web Developer', 'Cyber Security Analyst'],
    'skills': [
        'python sql excel data analysis',
        'java python c++ algorithms',
        'python machine learning deep learning tensorflow',
        'html css javascript react',
        'network security ethical hacking python'
    ]
})

def recommend_jobs(user_input):
    
    results = []
    for i, row in jobs.iterrows():
        count = sum(skill in row['skills'] for skill in user_input.lower().split())
        if count > 0:
            results.append((row['job_title'], count))
 
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:5]

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    if request.method == "POST":
        user_input = request.form["skills"]
        results = recommend_jobs(user_input)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
