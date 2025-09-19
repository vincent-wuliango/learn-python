from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def welcome_message():
    return "Halo, ini response dari server buatan gue!"

@app.route("/profile", methods=['GET', 'POST'])
def my_profile():
    if request.method == 'POST':
        incoming_data = request.get_json()
        name = incoming_data.get('name')

        response_data = {
            "message": f"Hello, {name}! Terima kasih sudah mengirim data."
        }
        return response_data

    else :
        my_data = {
            "full_name": "Vincent",
            "occupation": "Future Backend Engineer"
        }
    return my_data