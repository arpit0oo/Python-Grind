from flask import Flask, render_template, request # <--- NEW IMPORT: request
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

# UPDATED ROUTE: It now accepts "POST" methods (Envelopes)
@app.route("/generate", methods=["POST"])
def generate():
    # 1. Open the envelope and get the data by its name
    # We convert it to 'int' because inputs always send text strings
    length_from_form = int(request.form.get("length_data"))
    
    # 2. Use the number to generate the password
    password = gen_pass(length_from_form)
    
    # 3. Show the result
    return render_template("result.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)