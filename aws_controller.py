import boto3
import os
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
REGION_NAME = os.getenv("REGION_NAME")


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
def insert_item(id):  # first_name, last_name, gender, birthdate, mobile, email):
    response = CustomerTable.put_item(
        Item={
            "customer_id": id,
            # "first_name": first_name,
            # "last_name": last_name,
            # "gender": gender,
            # "mobile": mobile,
            # "birthdate": birthdate,
            # "email": email,
        }
    )
    return response


def get_itemfrom_id(id):
    response = CustomerTable.get_item(
        Key={"customer_id": id},
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


def delete_item(id):
    response = CustomerTable.delete_item(Key={"customer_id": id})
    return response
