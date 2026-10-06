# WEEK 13: CONSTRUCTING & RUNNING A BASIC RAG CHAIN
# Install:
# pip install langchain langchain-community langchain-openai faiss-cpu
 
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
 
print("===== WEEK 13: BASIC RAG CHAIN =====")
 
embeddings = OpenAIEmbeddings(
    api_key="YOUR_OPENAI_API_KEY"
)
 
vector_store = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)
 
retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)
 
llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="YOUR_OPENAI_API_KEY"
)
 
prompt = ChatPromptTemplate.from_template("""
Answer the question using only the given context.
 
Context:
{context}
 
Question:
{question}
 
Answer:
""")
 
parser = StrOutputParser()
chain = prompt | llm | parser
 
question = "What is Artificial Intelligence?"
 
documents = retriever.invoke(question)
 
context = "\n\n".join(
    [doc.page_content for doc in documents]
)
 
print("\n--- RETRIEVED CONTEXT ---")
print(context)
 
try:
    response = chain.invoke({
        "context": context,
        "question": question
    })
 
    print("\n--- RAG RESPONSE ---")
    print(response)
 
except Exception as e:
    print("\nError:", e)
 
