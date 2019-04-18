# Send custom metric data to cloudwatch
import boto3
import random

client = boto3.client('cloudwatch', region_name='eu-west-1')
value = float(random.randint(1,101))
print(value)

client.put_metric_data(
    MetricData=[
        {
            'MetricName': 'OpsMetric',
            'Dimensions': [
                {
                'Name': 'Instance Name',
                'Value': 'i-1234'
                }
            ],
            'Unit': 'None',
            'Value': value
            },
    ],
    Namespace = 'OpsNameSpace'
)