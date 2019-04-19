import json
import boto3
import logging
import time

def lambda_handler(event, context):
    # TODO implement
    asg_client = boto3.client('autoscaling')
    ec2_client = boto3.client('ec2', region_name='eu-west-1')
    ec2 = boto3.resource('ec2')
    
    print(json.dumps(event))
    message = event['detail']
    instance_id = message['EC2InstanceId']
    print(instance_id)
    
    instance = ec2.Instance(instance_id)
    for device in instance.block_device_mappings:
        volume = device.get('Ebs')
        print(volume.get('VolumeId'))
        root_snap_resp = ec2_client.create_snapshot(
                Description='My Snapshot Description',
                VolumeId=volume.get('VolumeId') 
            )
    response = asg_client.complete_lifecycle_action(
            LifecycleHookName='Vikram-Terminate-LC-Hook',
            AutoScalingGroupName='Vikram-AutoScaling-Group',
            LifecycleActionResult='CONTINUE'
        )
    print('Lifecycle event has been completed')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
