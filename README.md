# AWS-elasticbeastalk-FlaskAPI-Dynamodb-Codepipeline
[![Testing and Linting with Github Actions](https://github.com/Yayunyun/yayun_project4_awsAPI/actions/workflows/main.yml/badge.svg)](https://github.com/Yayunyun/yayun_project4_awsAPI/actions/workflows/main.yml)

This is yayun's repo for IDS706 project 4.
![alt text](https://github.com/Yayunyun/yayun_project4_awsAPI/blob/main/Blank%20board%20(5).png)


## API guide 
![This web app is host on AWS elastic beanstalk.] (http://Flaskdynamodbcustomer-env.eba-j26eetip.us-east-1.elasticbeanstalk.com)
Add the following term to the url to get, insert, and delete items from a dynamo db database. 
#### Get all customers information
```/get-items```
#### Get specific customer information
```/read-item/{customer id}```
#### Insert customers information
```/add-items/{customer id}/{customer first name}/customer last name}```
### Delete customer information
```/delete-item/{customer id}
