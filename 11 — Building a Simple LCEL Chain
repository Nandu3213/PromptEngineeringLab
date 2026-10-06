# WEEK 11: BUILDING A SIMPLE LCEL CHAIN
# Install:
# pip install langchain langchain-openai
 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
 
print("===== WEEK 11: SIMPLE LCEL CHAIN =====")
 
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words for a beginner engineering student."
)
 
llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="YOUR_OPENAI_API_KEY"
)
 
parser = StrOutputParser()
 
chain = prompt | llm | parser
 
topic = "Artificial Intelligence"
 
print("\nTopic:", topic)
 
try:
    response = chain.invoke({"topic": topic})
    print("\n--- LLM RESPONSE ---")
    print(response)
except Exception as e:
    print("\nError:", e)
 

