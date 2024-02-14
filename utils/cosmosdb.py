import os
import uuid
import datetime
import logging
import azure.cosmos.cosmos_client as cosmos_client
from azure.cosmos import CosmosClient, PartitionKey


url = os.getenv("COSMOS_DB_URL")
key = os.getenv("COSMOS_DB_KEY")

client = CosmosClient(url=url, credential=key)

database_name = 'CapeDB'
database = client.get_database_client(database_name)

container_name = 'CapeContainer'
container = database.get_container_client(container_name)


def save_chat(user_id, content, role):
    item = {
        'id': str(uuid.uuid4()),
        'timestamp': str(datetime.datetime.now()),
        'userId': user_id,
        'content': content,
        'role': role,
    }
    container.create_item(item)


def get_chat_history(user_id):
    query = f"SELECT TOP 5 * FROM c WHERE c.userId = '{user_id}' ORDER BY c.timestamp DESC"
    item_response = list(container.query_items(
        query=query,
        enable_cross_partition_query=True
    ))
    logging.info(item_response)
    history = []
    for item in item_response:
        history.append({
            "role": item["role"],
            "content": item["content"],
        })
    history.reverse()
    return history



