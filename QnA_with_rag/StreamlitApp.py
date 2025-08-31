import streamlit as st
from vectorstore_setup.vectorstore_build import get_query_engine
from QAWithPDF.data_ingestion import load_data
import os

def main():
    st.set_page_config("QA with Documents")
    save_folder='data'
    os.makedirs(save_folder,exist_ok=True)

    doc=st.file_uploader("Upload your document")
    if doc is not None:
        file_path=os.path.join(save_folder,doc.name)
        with open(file_path,'wb') as f:
            f.write(doc.getbuffer())
            f.close()

    st.header("QA with Documents(Information Retrieval)")

    user_question=st.text_input("Ask your question")

    if st.button("submit & process"):
        with st.spinner("Processing.."):
            
            document=load_data()
            query_engine=get_query_engine(document)

            response=query_engine.query(user_question)

            st.write(response.response)

if __name__=="__main__":
    main()
