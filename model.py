import pandas as pd
from langchain_pinecone import PineconeEmbeddings, PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec
from langchain.llms import OpenAI
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from dotenv import load_dotenv
import os
load_dotenv()

def invokeSearch(user_query):

    PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

    pc = Pinecone(api_key=PINECONE_API_KEY)

    index_name = "college-index"
    dimension = 1024  
    metric = "cosine"

    # Initialize Pinecone embeddings
    embeddings = PineconeEmbeddings(
        model="multilingual-e5-large",
        pinecone_api_key=PINECONE_API_KEY
    )
    
    # Initialize Pinecone vector store
    index = pc.Index(index_name)
    vector_store = PineconeVectorStore(index, embeddings, "text")

    llm = ChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        model_name='gpt-4o-mini',
        temperature=0.0
    )

    retriever = vector_store.as_retriever()

    template = """
    You are a college recommendation assistant. Based on the user's preferences and the college information provided, recommend and rank the top colleges. Explain why each college is recommended.
    
    User preferences: {query}
    
    College information:
    {context}
    
    Please provide a ranked list of recommended colleges with explanations:
    """

    PROMPT = PromptTemplate(
        template=template,
        input_variables=["query", "context"]
    )

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": PROMPT}
    )

    qa_chain = (
        {"context": retriever, "query": RunnablePassthrough()}
        | PROMPT
        | llm
    )    
    # user_query = "mathematics 34.783368,-86.568502 Normal,AL"
    result = qa_chain.invoke(user_query)
    return result
