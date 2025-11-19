import os
from src.llama import llama
from src.postgres_db import VectorDB
from dotenv import load_dotenv

load_dotenv()

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://ollama:11434")
MODEL = "tinyllama:1.1b" # Find available models here https://ollama.com/library
EMBEDDING_MODEL = "granite-embedding:30m" # Find available models here https://ollama.com/library

dbname=os.getenv("PGDATABASE", "postgres")
user=os.getenv("PGUSER", "user")
password=os.getenv("PGPASSWORD", "password")
host=os.getenv("PGHOST", "vector-postgres")
port=os.getenv("PGPORT", "5432")

vectordb = VectorDB(host=host, user=user, password=password, dbname=dbname, port=port)
llm = llama(OLLAMA_HOST, model=MODEL)

prompt="What is the capitol of France?"
print(llm.generate_response(prompt))
