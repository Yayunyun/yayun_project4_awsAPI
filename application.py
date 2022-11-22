from flask import Flask, jsonify, render_template
import aws_controller

application = Flask(__name__)  # create an app instance
app = application


@app.route("/")  # at the end point /
def hello():  # call method hello
    return render_template("base-template.html")  # which returns "hello world"


@app.route("/get-items")
def get_items():
    return jsonify(aws_controller.get_items())


if __name__ == "__main__":  # on running python app.py
    app.run()  # run the flask app
