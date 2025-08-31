import os
import sys
from dotenv import load_dotenv
from logger import logging
from exception import customexception
from config.constants import llm_model
from llama_index.llms.google_genai import GoogleGenAI
import google.generativeai as genai
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

def load_model():
    """
    Load a Gemini model for natural language processing.

    Returns:
    - Gemini: an instance of the Gemini llm model class
    """
    try:
        logging.info("load {llm_model} started...")
        genai.configure(api_key=google_api_key)
        model=GoogleGenAI(model=llm_model,api_key=google_api_key)
        logging.info("Successfully loaded LLM - {llm_model}")
        return model
    except Exception as e:
        logging.info("Model loaded process failed..")
        raise customexception(e,sys)
        