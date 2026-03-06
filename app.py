from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "OBIETTIVO LAVORO WEB APP ATTIVA"

if __name__ == "__main__":
    app.run()
