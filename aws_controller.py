import boto3
import os

# AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
# REGION_NAME = config("REGION_NAME")
AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
REGION_NAME = "us-east-1"

dynamo_client = boto3.client(
    "dynamodb",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION_NAME,
)

dynamo_resource = boto3.resource(
    "dynamodb",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION_NAME,
)

CustomerTable = dynamo_resource.Table("customer_table")


def get_items():
    return dynamo_client.scan(TableName="customer_table")


# first_name, last_name, gender, birthdate, email
def insert_item(id_insert):  # first_name, last_name, gender, birthdate, mobile, email):
    response = CustomerTable.put_item(
        Item={
            "customer_id": id_insert,
            # "first_name": first_name,
            # "last_name": last_name,
            # "gender": gender,
            # "mobile": mobile,
            # "birthdate": birthdate,
            # "email": email,
        }
    )
    return response


def get_itemfrom_id(id_get):
    response = CustomerTable.get_item(
        Key={"customer_id": id_get},
        AttributesToGet=[
            "first_name",
            "last_name",
            "gender",
            "mobile",
            "birthdate",
            "email",
        ],
    )
    return response


def delete_item(id_delete):
    response = CustomerTable.delete_item(Key={"customer_id": id_delete})
    return response
