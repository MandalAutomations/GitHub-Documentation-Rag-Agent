import os
from src.llama import llama
from src.postgres_db import VectorDB
from dotenv import load_dotenv

load_dotenv()

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://ollama:11434")
MODEL = "llama3.2:1b" # Find available models here https://ollama.com/library
EMBEDDING_MODEL = "granite-embedding:30m" # Find available models here https://ollama.com/library

dbname=os.getenv("PGDATABASE", "vector-postgres")
user=os.getenv("PGUSER", "vector-postgres")
password=os.getenv("PGPASSWORD", "vector-postgres")
host=os.getenv("PGHOST", "vector-postgres")
port=os.getenv("PGPORT", "vector-postgres")

vectordb = VectorDB(host=host, user=user, password=password, dbname=dbname, port=port)
llm = llama(OLLAMA_HOST, model=MODEL, embedding_model=EMBEDDING_MODEL)

