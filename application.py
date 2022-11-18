from flask import Flask  # import flask

application = Flask(__name__)  # create an app instance
app = application


@app.route("/")  # at the end point /
def hello():  # call method hello
    return "Hello MIDS!"  # which returns "hello world"


# if __name__ == "__main__":        # on running python app.py
#     app.run()                     # run the flask app
