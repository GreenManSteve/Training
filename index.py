import json
import datetime


def handler(event, context):
    id = event['id']
    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'id': id
    }
    print("Lambdaaaaaaaaaaa", context.invoked_function_arn)
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
