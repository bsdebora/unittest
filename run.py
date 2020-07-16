import os
import json
from flask import Flask , render_template, request, flash

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ourspecialities")
def ourspecialities():
    data = []
    with open("data/dishes.json","r") as json_data:
        data = json.load(json_data)
    return render_template("ourspecialities.html", page_title="Our Specialities", dishes =data)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method =="POST":
        flash("Thank you {}, we have recieved your message!".format(request.form["name"]))
    return render_template("contact.html", page_title = "Contact Us")


@app.route("/careers")
def careers():
    return render_template("careers.html", age_title = "Come work with us")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

