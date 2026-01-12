from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

@app.route("/user")
def user_list():
    return "<p>User List</p>"

@app.route("/class")
def class_list():
    return "<p>Class List</p>"

@app.route("/teacher")
def teacher_list():
    return "<p>Teacher List</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
