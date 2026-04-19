import unittest
from unittest.mock import Mock, call

from src.app import lambda_handler


class TestLambdaHandler(unittest.TestCase):
    def test_inserts_message_body_for_each_record(self):
        table = Mock()
        event = {
            "Records": [
                {"messageId": "id-1", "body": "hello"},
                {"messageId": "id-2", "body": "world"},
            ]
        }

        result = lambda_handler(event, None, table=table)

        table.put_item.assert_has_calls(
            [
                call(Item={"MessageId": "id-1", "MessageBody": "hello"}),
                call(Item={"MessageId": "id-2", "MessageBody": "world"}),
            ]
        )
        self.assertEqual(result, {"processed": 2})

    def test_defaults_message_body_when_missing(self):
        table = Mock()
        event = {"Records": [{"messageId": "id-1"}]}

        lambda_handler(event, None, table=table)

        table.put_item.assert_called_once_with(
            Item={"MessageId": "id-1", "MessageBody": ""}
        )


if __name__ == "__main__":
    unittest.main()
