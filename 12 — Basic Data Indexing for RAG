# WEEK 12: BASIC DATA INDEXING FOR RAG
# Install:
# pip install langchain langchain-community langchain-openai faiss-cpu pypdf
 
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
 
print("===== WEEK 12: BASIC DATA INDEXING FOR RAG =====")
 
loader = TextLoader("sample.txt", encoding="utf-8")
documents = loader.load()
 
print("\nDocument loaded successfully.")
 
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
 
chunks = text_splitter.split_documents(documents)
 
print("Number of chunks:", len(chunks))
 
embeddings = OpenAIEmbeddings(
    api_key="YOUR_OPENAI_API_KEY"
)
 
vector_store = FAISS.from_documents(
    chunks,
    embeddings
)
 
print("Vector database created successfully.")
 
vector_store.save_local("faiss_index")
 
print("FAISS index saved successfully.")

