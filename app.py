from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Secure DevSecOps Pipeline Project"

@app.route("/login", methods=["GET", "POST"])
def login():
    hardcoded_password = "123456"  # intentional vulnerability

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if password == hardcoded_password:
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
    app.run(debug=True)
