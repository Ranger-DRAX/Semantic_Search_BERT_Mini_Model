import streamlit as st
#import pythorch as pt
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer

indexName = "all_products"

try:
    es = Elasticsearch(
        "https://localhost:9200",
        basic_auth=("elastic", "mb8gn4HBQfKyRV7nt+RG"),
        ca_certs=r"E:\Semantic_Search_Vector(BERT)_Embadding\elasticsearch-9.0.0\config\certs\http_ca.crt"
    )
except ConnectionError as e:
    print("Connection Error:", e)

if es.ping():
    print("Successfully connected to ElasticSearch!!")
else:
    print("Oops!! Can not connect to Elasticsearch!")

# Load model once at the top
model = SentenceTransformer('multi-qa-mpnet-base-dot-v1')

def search(input_keyword):
    vector_of_input_keyword = model.encode(input_keyword).tolist()  # ensure it's list

    query = {
        "size": 20,
        "_source": ["ProductName", "Description"],
        "query": {
            "knn": {
                "field": "DescriptionVector",  # Ensure this matches the field name in your index mapping
                "query_vector": vector_of_input_keyword ,
                "k": 10,
                "num_candidates": 500 # Optional: Adjust based on your requirements
            }
        }
    }

    res = es.search(index="all_products", body=query)

    return res['hits']['hits']

def main():
    st.title("Searching _Fashion Products")

    search_query = st.text_input("Enter your search query")

    if st.button("_Search_"):
        if search_query:
            results = search(search_query)

            st.subheader("Search Results")
            for result in results:
                with st.container():
                    source = result.get('_source', {})
                    st.header(source.get('ProductName', 'No Product Name Found'))
                    st.write(f"Description: {source.get('Description', 'No Description')}")
                    st.divider()

if __name__ == "__main__":
    main()
