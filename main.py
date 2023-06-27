import os
import json

with open("config.json") as file:
    config_data = json.load(file)
    
os.environ["OPENAI_API_KEY"] = config_data["api_keys"]["open_ai"]

from llama_index import VectorStoreIndex, SimpleDirectoryReader

while True:
    query = input("\nQuestion: ")

    documents = SimpleDirectoryReader('data').load_data()
    index = VectorStoreIndex.from_documents(documents)

    query_engine = index.as_query_engine()
    response = query_engine.query(query)

    print(response)
