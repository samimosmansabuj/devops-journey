from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

@app.route("/user")
def user_list():
    return "<p>User List</p>"

if __name__ == "__main__":
    app.run(debug=True)
