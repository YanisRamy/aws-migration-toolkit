import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import json
from unittest.mock import patch, MagicMock
import handler

def test_lambda_handler_success():
    event = {
        "Records": [{
            "s3": {
                "bucket": {"name": "test-bucket"},
                "object": {"key": "test-file.txt", "size": 1024}
            }
        }]
    }

    with patch('handler.dynamodb') as mock_dynamodb:
        mock_table = MagicMock()
        mock_dynamodb.Table.return_value = mock_table

        response = handler.lambda_handler(event, None)

        assert response['statusCode'] == 200
        body = json.loads(response['body'])
        assert 'test-file.txt' in body['message']
        mock_table.put_item.assert_called_once()

def test_lambda_handler_error():
    event = {"Records": []}
    response = handler.lambda_handler(event, None)
    assert response['statusCode'] == 500

if __name__ == '__main__':
    test_lambda_handler_success()
    test_lambda_handler_error()
    print("Tous les tests sont passés ✓")
