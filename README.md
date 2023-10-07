## Objectives
<br />To create data in a Kinesis stream that can be copied to the
DynamoDB database.

## Solution
![Image](https://github.com/huyphamch/terraform-aws-create-scalable-web-rds/blob/master/diagrams/AWS_architecture.drawio.png)
<br />Create Kinesis stream.
<br />Create Lambda function to store Kinesis events in the DynamoDB.
<br />Grant Permission to the Lambda function to access the Kinesis stream and write logs to CloudWatch.

## Usage
<br /> 1. Open terminal
<br /> 2. Before you can execute the terraform script, your need to configure your aws environment first.
<br /> aws configure
<br /> AWS Access Key ID: See IAM > Security credentials > Access keys > Create access key
<br /> AWS Secret Access Key: See IAM > Security credentials > Access keys > Create access key
<br /> Default region name: us-east-1
<br /> Default output format: json
<br /> 3. Now you can apply the terraform changes.
<br /> terraform init
<br /> terraform apply --auto-approve
<br /> Result: The Kinesis stream and Lambda function are created and ready to consume events.
<br /> 4. Open [Colaboratory](https://colab.research.google.com) and create new Notebook.
<br /> 5. Execute command: pip install boto3
<br /> 6. Execute script: [realtime_data_produce.py](./code/realtime_data_produce.py)
<br />  Result: Events are written to Kineses.
<br />  Result: Events are stored in the DynamoDB.
<br /> 7. At the end you can cleanup the created AWS resources.
<br /> terraform destroy --auto-approve
