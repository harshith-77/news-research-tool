import streamlit as st
import pickle
import os
import logging
from dotenv import load_dotenv

import langchain
from langchain.chains import RetrievalQAWithSourcesChain
from langchain_community.llms import Ollama
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings

import helper

langchain.debug = True
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
load_dotenv()

# url loading -> text splitting -> create embeddings and storing in vector index / database -> retrieval relevant chunks according to the question

# Loading Embeddings Model
embeddings = HuggingFaceEmbeddings()
# Loading LLM Model
# llm = Ollama(model="mistral:7b-instruct-v0.3-q2_K")
llm = GoogleGenerativeAI(model='gemini-2.0-flash-exp', google_api_key=os.environ['GEMINI_API_KEY'])

st.title("News Research Tool")

urls = []
st.sidebar.title("News Article URLs")
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}:")
    urls.append(url)
process_urls = st.sidebar.button("Process URLs")

main_place_holder = st.empty()
file_name = "vectorIndex.pkl"
if process_urls:
    try:
        if os.path.exists(file_name):
            os.remove(file_name)

        #Loading URLs
        logging.info("Loading URLs")
        main_place_holder.text("Loading URLs")
        data = helper.url_loader(urls)

        #Splitting into Chunks
        logging.info("Splitting into Chunks")
        main_place_holder.text("Splitting into Chunks for better retrieval")
        docs = helper.text_splitter(data, chunk_size=200, chunk_overlap=50)

        #Creating embeddings and Inserting into vector store
        logging.info("Creating embeddings and Inserting into vector store")
        main_place_holder.text("Creating embeddings and Inserting into Vector store")
        vector_store_index = helper.indexer(docs, embeddings)

        #Saving the vector store onto the disk
        logging.info("Saving the vector store onto the disk")
        main_place_holder.text("Saving the vector store")
        with open(file_name, 'wb') as f:
            pickle.dump(vector_store_index, f)
    except Exception as e:
        logging.exception(f"Error occurred while creating vector index: {e}")

query = main_place_holder.text_input("Question: ")
if query:
    try:
        logging.info("Answering the question")
        if os.path.exists(file_name):
            with open(file_name, 'rb') as f:
                vector_index = pickle.load(f)

        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vector_index.as_retriever(), verbose=True, reduce_k_below_max_tokens=True)
        result = chain.invoke({"question":query})

        st.header("Answer: ")
        st.write(result["answer"])
        logging.info(f"Answer: {result["answer"]}")

        sources = result.get("sources", "")
        if sources:
            st.subheader("Sources: ")
            sources_list = sources.split("\n")
            for source in sources_list:
                st.write(source)
    except Exception as e:
        logging.exception(f"Error occurred while generating answer: {e}")