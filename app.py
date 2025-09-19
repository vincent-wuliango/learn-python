from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome_message():
    return "Halo, ini response dari server buatan gue!"

@app.route("/profile")
def my_profile():
    my_data = {
        "full_name": "Vincent",
        "occupation": "Future Backend Engineer"
    }

    return my_data