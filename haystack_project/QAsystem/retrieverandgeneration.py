from haystack.utils import Secret
from haystack.components.embedders import SentenceTransformersTextEmbedder
from haystack.components.builders import ChatPromptBuilder
from haystack.dataclasses import ChatMessage
from haystack_integrations.components.retrievers.pinecone import PineconeEmbeddingRetriever
from haystack.components.generators.chat import OpenAIChatGenerator
from haystack import Pipeline
import os
from dotenv import load_dotenv
from QAsystem.utils import pinecone_config
load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

template=[ChatMessage.from_user("""
 Answer the following query based on the provided context. If the context does
                     not include an answer, reply with 'I don't know'.\n
                     Query: {{query}}
                     Documents:
                     {% for doc in documents %}
                        {{ doc.content }}
                     {% endfor %}
                     Answer: 
"""
)]

def get_result(query):
    query_pipeline=Pipeline()

    query_pipeline.add_component("text_embedder",SentenceTransformersTextEmbedder())
    query_pipeline.add_component("retriever",PineconeEmbeddingRetriever(document_store=pinecone_config()))
    query_pipeline.add_component("prompt_builder",ChatPromptBuilder(template=template))
    query_pipeline.add_component("llm",OpenAIChatGenerator(model='gpt-4o'))

    query_pipeline.connect("text_embedder.embedding","retriever.query_embedding")
    query_pipeline.connect("retriever.documents","prompt_builder.documents")
    query_pipeline.connect("prompt_builder.prompt","llm.messages")

    result=query_pipeline.run(
        {
            "text_embedder":{"text":query},
            "prompt_builder":{"query":query}
        }
    )

    response=result["llm"]["replies"][0].text
    return response


if __name__=='__main__':
    query="What is transformers?"
    response=get_result(query)
    print(response)