from flask import Flask, make_response, redirect, render_template, request, url_for
import pickle
import os

flask_app = Flask(__name__)

@flask_app.route('/')
def redirect_to_home():
    return redirect(url_for('home'))

@flask_app.route('/home')
def home():
    return render_template("home.html")

@flask_app.route('/process-text', methods=["POST"])
def process_text():
    # Get the text from the form input
    user_text = request.form.get('text')
    
    # Process the text (you can perform any logic here)
    if user_text:
        with open(os.path.join(os.getcwd(), "model/modelo.pkl"), 'rb') as modelo_file:
            cv, le, modelo = pickle.load(file=modelo_file)
        predictions = le.inverse_transform(modelo.predict(cv.transform([user_text])))[0]
        response_message = f"Idioma predicho: {predictions}"
    else:
        response_message = "No text received"
    
    # Pass the message to the template and render the page with the message
    return render_template('home.html', response_message=response_message)

if __name__ == '__main__':
    flask_app.run(host="0.0.0.0", port=8000, debug=True)