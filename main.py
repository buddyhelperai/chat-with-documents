import os
import json

with open("config.json") as file:
    config_data = json.load(file)

os.environ["OPENAI_API_KEY"] = config_data["api_keys"]["open_ai"]

from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader('data').load_data()
index = GPTVectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
response = query_engine.query("write a text with the indications you have, with the information on which to write the text.")

print(response.response)
