# aws-python-flask-app
Sample Python Flask Application for AWS work

- custom-metric - A simple script that sends custom metric data to cloudwatch
- Creates a dynamodb table 'customer' using .ebextensions 
- cf-pipeline - Contains a cloudformation template to create a build and deploy pipeline

### Commands for CF
- Validate Template
aws cloudformation validate-template --template-body file://configure-pipeline.yaml
- Create Stack
aws cloudformation create-stack --stack-name aws-python-flask-app-stack --template-body file://configure-pipeline.yaml
