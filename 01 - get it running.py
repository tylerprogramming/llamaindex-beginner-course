from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Without this, LlamaIndex 0.11 answers with gpt-3.5-turbo, which OpenAI shut down.
Settings.llm = OpenAI(model="gpt-4o")

documents = SimpleDirectoryReader("pdf/").load_data()

index = VectorStoreIndex.from_documents(documents) 

query_engine = index.as_query_engine()

response = query_engine.query("What are the design goals and give details about it please.")

print(response)