# Chat with documents

Example code based on llama_index libray, to "chat with" plain text files included in the /data directory

## Install llama-index on Ubuntu
<code>pip install llama-index</code>

## main.py
1) Imports the os and json modules.
2) Loads the JSON data from the config.json file into the config_data variable.
3) Sets the "OPENAI_API_KEY" environment variable using the value from config_data.
4) Imports the VectorStoreIndex and SimpleDirectoryReader classes from the llama_index module.
5) Loads the documents from the "data" directory using a SimpleDirectoryReader object and assigns them to the documents variable.
6) Creates a search index VectorStoreIndex from the documents variable and assigns it to the index variable.
7) Creates a query engine query_engine from the index variable.
8) Executes a query on the query_engine with a specified query string and prints the response

## OpenAI Api Key
In order to run this example, you need an OpenAI Api Key. With an OpenAI working account, go to https://platform.openai.com/account/api-keys and generate a valid key. Paste the key into config.js

## Run
Simply download the Python code, paste a valid OpenAI Api Key into config.js and run <code>python main.py</code>

<a href="http://www.youtube.com/watch?feature=player_embedded&v=u-wJoZ4sA88" target="_blank"><img src="http://img.youtube.com/vi/u-wJoZ4sA88/0.jpg" alt="" width="480" height="269" border="10"></a>

https://www.youtube.com/watch?v=u-wJoZ4sA88
