from flask import Flask, send_from_directory, render_template  # type: ignore
import os

app = Flask(__name__, template_folder='main/template')  # Specify template folder

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<filename>')
def send_file(filename):
    return send_from_directory('main/static', filename)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)  # Change here: host="0.0.0.0"
