import sys
sys.dont_write_bytecode = True
from flask import Flask, render_template

app = Flask(__name__)

# Your HuggingFace Space URL
SPACE_URL = "https://MIRNA-MOUKHTAR2025-space-inspiration.hf.space"

@app.route("/")
def home():
    return render_template("index.html", space_url=SPACE_URL)

if __name__ == "__main__":
    app.run(debug=True ,port=8000)
