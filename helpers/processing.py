import tiktoken
import glob
import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def convert_string_to_chunks(knowledge_base, model):
  encoding = tiktoken.encoding_for_model(model_name=model)

  tokens = encoding.encode(knowledge_base)

  return tokens


def split_files(base_dir):
  documents = []

  folders = glob.glob(f"{base_dir}/**")

  for folder in folders:
    doc_type = os.path.basename(folder)
    loader = DirectoryLoader(folder, glob="**/*", loader_cls=TextLoader, loader_kwargs={'encoding': 'utf-8'})
    folder_docs = loader.load()

    for doc in folder_docs:
      doc.metadata["doc_type"] = doc_type
      documents.append(doc)

  return documents

def convert_docs_to_chunks(documents):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
  chunks = text_splitter.split_documents(documents)

  return chunks