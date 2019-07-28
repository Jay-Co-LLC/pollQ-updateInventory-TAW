import json
import boto3

sqs = boto3.resource('sqs')

def lambda_handler(event, context):
    
    q = sqs.get_queue_by_name(QueueName='q-updateInventory-TAW')
    numChunksFinished = q.attributes['ApproximateNumberOfMessages']
    
    return {
            'statusCode' : 200,
            'headers' : {
                'Access-Control-Allow-Origin' : '*'
            },
            'body' : json.dumps({'numChunksFinished' : numChunksFinished})
        }
