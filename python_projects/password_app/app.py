from flask import Flask, render_template, request
import random
import sqlite3


app = Flask(__name__)

def app_db():
    conn = sqlite3.connect("history.db")
    cursor=conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT,
            strength TEXT
        )
    """)
    conn.commit()
    conn.close()
app_db()
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
    
    conn = sqlite3.connect("history.db")
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO passwords (content, strength) VALUES (?, ?)", (password, strength))
    
    conn.commit()
    conn.close()
    
    password = gen_pass(length_from_form)
    return render_template("result.html", password=password, strength=strength)
@app.route("/history")
def history():
    # 1. Connect to the database
    conn = sqlite3.connect("history.db")
    cursor = conn.cursor()
    
    # 2. Get ALL passwords (ordered by newest first)
    cursor.execute("SELECT * FROM passwords ORDER BY id DESC")
    data = cursor.fetchall()
    
    # 3. Close connection
    conn.close()
    
    # 4. Show the History page (sending the data list)
    return render_template("history.html", history_data=data)

if __name__ == "__main__":
    app.run(debug=True)