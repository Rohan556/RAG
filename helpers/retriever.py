from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
import os

def provide_retriever_result(question):
  load_dotenv(override=True)
  OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

  # if OPENAI_API_KEY:
  #   print(f"OpenAI API key exists with {OPENAI_API_KEY[:8]}")

  # else:
  #   print("Key not found")

  db_name = "vector_db"

  embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

  vectorstore = Chroma(persist_directory=db_name, embedding_function=embeddings)

  retreiver = vectorstore.as_retriever(
    search_kwargs = {"k": 4}
  )

  retriever_result = retreiver.invoke(question)

  return retriever_result



