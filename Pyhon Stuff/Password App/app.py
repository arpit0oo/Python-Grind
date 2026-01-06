from flask import Flask, render_template, request
import random

app = Flask(__name__)

def gen_pass(length):
    password = ""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%"
    for i in range(length):
        char = random.choice(chars)
        password = password + char
    return password

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/generate", methods=["POST"])
def generate():
    length_from_form = int(request.form.get("length_data"))
    if length_from_form>=12:
        strength = "STRONG"
    else:
        strength = "WEAK"
    
    password = gen_pass(length_from_form)
    return render_template("result.html", password=password, strength=strength)

if __name__ == "__main__":
    app.run(debug=True)