import streamlit as st
import os
from QAsystem.retrieverandgeneration import get_result

def main():
    st.set_page_config("QA with Documents")
    st.header("QA with Haystack")

    user_question=st.text_input("Ask your question")

    if st.button("submit & process"):
        with st.spinner("Processing.."):
            response=get_result(user_question)
            st.write(response)

if __name__=="__main__":
    main()
