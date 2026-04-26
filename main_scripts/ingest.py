from helpers import files, processing, embedding

def ingest():
  files_in_dir = files.get_all_files_from_directory("knowledge-base")
  print(f"Found {len(files_in_dir)} in the provided directory")

  entire_knowledge_base = files.combine_files(files_in_dir)

  tokens = processing.convert_string_to_chunks(knowledge_base=entire_knowledge_base, model="gpt-4.1-nano")
  print(f"Total tokens for the provided knowledge base is {len(tokens)}")
  

  documents = processing.split_files(base_dir="knowledge-base")
  print(f"It has {len(documents)} number of docs")

  chunks = processing.convert_docs_to_chunks(documents)
  print(f"Divided into {len(chunks)} chunks")
  print(f"First chunk {chunks[0]}")

  vector_store = embedding.create_and_store_embeddings(db_name="vector_db", chunks=chunks)
  print(f"Vector store created with {vector_store._collection.count():,} documents")

ingest()