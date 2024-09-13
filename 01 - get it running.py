import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

os.environ["OPENAI_API_KEY"] = "sk-proj-1111"

documents = SimpleDirectoryReader("pdf/").load_data()

index = VectorStoreIndex.from_documents(documents) 

query_engine = index.as_query_engine()

print(query_engine.query("What are the design goals and give details about it please."))










