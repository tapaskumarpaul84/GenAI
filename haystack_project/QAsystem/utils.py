from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["HF_API_TOKEN"]=os.getenv("HF_API_TOKEN")
os.environ["PINECONE_API_KEY"]=os.getenv("PINECONE_API_KEY")

def pinecone_config():
    document_store=PineconeDocumentStore(
        index='default',
        namespace='default',
        dimension=768
    )
    return document_store