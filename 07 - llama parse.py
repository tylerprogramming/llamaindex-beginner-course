import nest_asyncio
from dotenv import load_dotenv

nest_asyncio.apply()
load_dotenv()  # LLAMA_CLOUD_API_KEY (and OPENAI_API_KEY) from .env

from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

parser = LlamaParse(
    # LlamaParse reads the key from the LLAMA_CLOUD_API_KEY environment variable
    result_type="markdown",  # "markdown" and "text" are available
    verbose=True,
)

file_extractor = {".pdf": parser}
documents = SimpleDirectoryReader(
    "./pdf", file_extractor=file_extractor
).load_data()

index = VectorStoreIndex.from_documents(documents) 
index.storage_context.persist(persist_dir="storage")

query_engine = index.as_query_engine()

response = query_engine.query("What are the design goals and give details about it please.")

print(response)


