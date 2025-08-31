import os
import sys
from dotenv import load_dotenv
from logger import logging
from exception import customexception
import google.generativeai as genai
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from config.constants import embedding_model
load_dotenv()


try:
    logging.info("API key load strated..")
    google_api_key=os.getenv("GOOGLE_API_KEY")
    if google_api_key !="":
        logging.info("API key loaded....")
    else:
        logging.info("API key not available")
except Exception as e:
    logging.ingo("Error in loading api key")
    raise customexception(e,sys)

def load_gemini_embedding():
    """
    Load the embedding model from Gemini 

    Returns:
    - Gemini: an instance of containg the embedding model.
    """
    try:
        logging.info("Embedding model loading started....")
        genai.configure(api_key=google_api_key)
        embed_model=GoogleGenAIEmbedding(model_name=embedding_model,api_key=google_api_key)
        logging.info("Embedding model loaded successfully.")
        return embed_model
    except Exception as e:
        logging.info("Failed to load embedding model from Gemini.")
        raise customexception(e,sys)
    
