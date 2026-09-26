import json
import boto3
import os
from datetime import datetime

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

BUCKET_NAME = os.environ.get('BUCKET_NAME', 'aws-migration-toolkit-uploads')
TABLE_NAME = os.environ.get('TABLE_NAME', 'aws-migration-toolkit-events')

def lambda_handler(event, context):
    """
    Déclenchée par un événement S3 (ObjectCreated).
    Enregistre les métadonnées du fichier uploadé dans DynamoDB.
    """
    try:
        record = event['Records'][0]
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        size = record['s3']['object']['size']

        table = dynamodb.Table(TABLE_NAME)
        table.put_item(Item={
            'event_id': f"{bucket}/{key}/{datetime.utcnow().isoformat()}",
            'bucket': bucket,
            'file_key': key,
            'file_size': size,
            'processed_at': datetime.utcnow().isoformat(),
            'status': 'PROCESSED'
        })

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f'File {key} processed successfully',
                'size': size
            })
        }
    except Exception as e:
        print(f"Error processing event: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
