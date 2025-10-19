import os
from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect

# Ensure the instance folder exists (for SQLite file)
os.makedirs("instance", exist_ok=True)

app = Flask(__name__)

# Load secrets from environment (python-dotenv will read .env in dev)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-key")
app.config["WTF_CSRF_TIME_LIMIT"] = None  # simpler in dev

csrf = CSRFProtect(app)

@app.route("/")
def index():
    return render_template("base.html", message="Secure Login Demo")

if __name__ == "__main__":
    # Debug=True auto-restarts on code changes
    app.run(debug=True)
