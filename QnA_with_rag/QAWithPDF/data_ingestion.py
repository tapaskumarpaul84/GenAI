from llama_index.core import SimpleDirectoryReader
from exception import customexception
from logger import logging
import sys
import os
from pathlib import Path

def load_data():
    """
    Load data documents from a specified directory.

    Parameters:
    - data (str) : The path to the directory containing PDF files.

    Returns:
    - A list of loaded PDF documents. The specific type of documents may vary.
    """
    try:
        logging.info("Data loading started...")
        loader=SimpleDirectoryReader('data')
        documents=loader.load_data()
        print("file loaded")
        logging.info("data loading completed..")
        return documents
    except Exception as e:
        print("load failed")
        logging.info("exception in data loading....")
        raise customexception(e,sys)
    

if __name__=="__main__":
    #data_path='F:\Tapas\Learning\GenAI\QnA_with_rag\data\2410.12837v1.pdf'
    load_data(data_path=None)