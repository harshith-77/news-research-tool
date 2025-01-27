import logging
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def url_loader(urls):
    try:
        loader = UnstructuredURLLoader(urls=urls, show_progress_bar=True)
        data = loader.load()
        logging.info(f"Loaded URLs: {data}")
        return data
    except Exception as e:
        logging.exception(f"Exception occurred in url_loader {e}")

def text_splitter(data, chunk_size, chunk_overlap):
    try:
        splitter = RecursiveCharacterTextSplitter(["\n\n", "\n"], chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        chunks = splitter.split_documents(data)
        logging.debug(f"First 5 Chunks: {chunks[:5]}")
        return chunks
    except Exception as e:
        logging.exception(f"Exception occurred in url_loader {e}")

def indexer(docs, embeddings):
    try:
        vector_store_index = FAISS.from_documents(docs, embeddings)
        return vector_store_index
    except Exception as e:
        logging.exception(f"Exception occurred in url_loader {e}")