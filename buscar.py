import os
import pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.pinecone import Pinecone

def main():
    pinecone.init(api_key="fc1c7b01-da90-4480-8599-ae80124757b9", environment="gcp-starter")
    embeddings = OpenAIEmbeddings()
    text = open("documentos/economia.txt", "r", encoding="utf8")
    #print(text.read())
    # pinecone.create_index("gpt", dimension=1536, metric="cosine")
    data = Pinecone.from_texts(texts=[text.read()], embedding=embeddings, index_name='gpt')
    text = open("documentos/ingenieria-civil.txt", "r", encoding="utf8")
    data = Pinecone.from_texts(texts=[text.read()], embedding=embeddings, index_name='gpt')
    text = open("documentos/ingenieria-sistemas.txt", "r", encoding="utf8")
    data = Pinecone.from_texts(texts=[text.read()], embedding=embeddings, index_name='gpt')
    text = open("documentos/ingenieria-electrica.txt", "r", encoding="utf8")
    data = Pinecone.from_texts(texts=[text.read()], embedding=embeddings, index_name='gpt')
    text = open("documentos/ingenieria-industrial.txt", "r", encoding="utf8")
    data = Pinecone.from_texts(texts=[text.read()], embedding=embeddings, index_name='gpt')

def buscar():
    pinecone.init(api_key="fc1c7b01-da90-4480-8599-ae80124757b9", environment="gcp-starter")
    embeddings = OpenAIEmbeddings()
    # if you already have an index, you can load it like this
    docsearch = Pinecone.from_existing_index("gpt", embeddings)
    query = "Cuantos años de acreditación tiene ingeniería de industrial?"
    docs = docsearch.similarity_search(query)
    print(docs)

if __name__ == "__main__":
     main()