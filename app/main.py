from fastapi import FastAPI, Response, Request
from flask import Flask, make_response, redirect, render_template, request
import uvicorn

app = FastAPI(debug=True)

flask_app = Flask(__name__)

@flask_app.route('/')
def redirect_to_home():
    response = make_response(redirect('/home'))
    return response

@flask_app.route('/home')
def home():
    return render_template("home.html")

@app.post('/translate-text')
def translate(user_text):
    pass

@flask_app.route('/process-text', methods=["POST"])
def process_text():
    user_text = request.form.get('text')
    pass

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
