
from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = "1.0"

@app.route("/")
def home():
    return f"""
    <html>
        <head>
            <title>AWS DevOps Project</title>
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 100px;">
            <h1>AWS DevOps Automation Platform</h1>
            <h2>Hello from Flask!</h2>
            <p>Application Version: {APP_VERSION}</p>
            <p>Status: Running Successfully</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(
        status="healthy",
        version=APP_VERSION
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
