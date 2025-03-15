from flask import Flask, send_from_directory # type: ignore

app = Flask(__name__)

@app.route('/static/<filename>')
def send_file(filename):
    return send_from_directory('static', filename)

if __name__ == "__main__":
    app.run(debug=True)
