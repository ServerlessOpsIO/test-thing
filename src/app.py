import os
import uuid


def _resolve_table(table):
    if table is not None:
        return table

    import boto3

    return boto3.resource("dynamodb").Table(os.environ["TABLE_NAME"])


def lambda_handler(event, _context, table=None):
    dynamodb_table = _resolve_table(table)
    records = event.get("Records", [])

    for record in records:
        dynamodb_table.put_item(
            Item={
                "MessageId": record.get("messageId") or str(uuid.uuid4()),
                "MessageBody": record.get("body", ""),
            }
        )

    return {"processed": len(records)}
