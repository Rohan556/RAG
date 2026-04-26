from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv

def create_and_store_embeddings(db_name, chunks):
  load_dotenv(override=True)
  OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

  if OPENAI_API_KEY:
    print(f"OpenAI API key exists with {OPENAI_API_KEY[:8]}")

  else:
    print("Key not found")

  embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

  if os.path.exists(db_name):
    Chroma(persist_directory=db_name, embedding_function=embeddings).delete_collection()

  vector_store = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=db_name)

  return vector_store