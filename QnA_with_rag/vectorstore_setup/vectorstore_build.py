import sys
import os
from logger import logging
from exception import customexception
from QAWithPDF.embedding import load_gemini_embedding
from QAWithPDF.model_api import load_model
from config.constants import chunk_size,chunk_overlap,num_output,context_window
from llama_index.core import Settings
from llama_index.core import VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter


def get_query_engine(documents):
    """
    make a vectorstore with the given documents and embedding model.

    return:
    a query engine with the llm for QnA system.
    """
    try:
        logging.info("Started building the query engine....")
        Settings.llm=load_model()
        Settings.embed_model=load_gemini_embedding()
        Settings.transformations=[SentenceSplitter(chunk_size=chunk_size,chunk_overlap=chunk_overlap)]
        Settings.num_output=num_output
        Settings.context_window=context_window
        index=VectorStoreIndex.from_documents(documents)
        index.storage_context.persist()
        query_engine=index.as_query_engine()
        logging.info("Successfully query_engine built.")
        return query_engine
    except Exception as e:
        logging.info("Query engine failed to develop")
        raise customexception(e,sys)
    
    

