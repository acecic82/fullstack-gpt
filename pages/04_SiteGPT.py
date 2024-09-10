import streamlit as st

from langchain.document_loaders import SitemapLoader

st.title("SiteGPT")

st.write("Ask questions about the content of a website.")
st.write("Start by writing the URL of the website on the sidebar.")


with st.sidebar:
    url = st.text_input("Write down a URL", placeholder="https://example.com")

if url:
    if ".xml" not in url:
        with st.sidebar:
            st.error("Please write down a Sitemap URL.")
    else:
        loader = SitemapLoader(url)
        loader.requests_per_second = 2
        docs = loader.load()
        st.write(docs)
