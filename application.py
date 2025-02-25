from flask import Flask, render_template
import aws_controller

application = Flask(__name__)  # create an app instance
app = application


@app.route("/")  # at the end point /
def hello():  # call method hello
    return render_template("base-template.html")  # which returns "hello world"


@app.route("/get-items")
def get_items():
    response = aws_controller.get_items()
    return response['Items']


@app.route("/add-item/<string:id_add>/")
def add_item(id_add):
    # check if the id already exist
    response_check = aws_controller.get_itemfrom_id(id_add)
    if response_check["ResponseMetadata"]["HTTPStatusCode"] == 200:
        if "Item" in response_check:
            return "This customer already existx", {"Item": response_check["Item"]}

    # If the customer does not exist, add new customer information
    response = aws_controller.insert_item(id_add)
    if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
        return {
            "msg": "Added successfully",
        }
    return {"msg": "Some error occcured", "response": response}


@app.route("/read-item/<string:id_read>")
def read_item(id_read):
    response = aws_controller.get_itemfrom_id(id_read)

    if response["ResponseMetadata"]["HTTPStatusCode"] == 200:

        if "Item" in response:
            return {"Item": response["Item"]}

        return {"msg": "Customer not found!"}

    return {"msg": "Some error occured", "response": response}


@app.route("/delete-item/<string:id_delete>")
def delete_item(id_delete):
    response = aws_controller.delete_item(id_delete)

    if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
        return {
            "msg": "Deleted successfully",
        }

    return {"msg": "Some error occcured", "response": response}


if __name__ == "__main__":  # on running python app.py
    app.run()  # run the flask app
