from flask import Flask, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)



@app.route("/")
def ibm():
    return render_template("ibm.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/story")
def story():
    return render_template("story.html")

@app.route("/report")
def report():
    return render_template("report.html")

if __name__ == "__main__":
   app.run(debug=True)