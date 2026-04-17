from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Secure DevSecOps Pipeline Project"

@app.route("/login", methods=["GET", "POST"])
def login():
    stored_password = os.getenv("APP_PASSWORD", "defaultpassword")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if password == stored_password:
            return f"Welcome, {username}"
        else:
            return "Invalid credentials", 401

    return render_template("login.html")

@app.route("/api/status")
def status():
    return jsonify({
        "status": "running",
        "service": "devsecops-demo-app"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)