from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

openai_client=OpenAI(
    api_key = "AIzaSyBmcY5YU_ab25xdMzf9NEv_vizyZ5pDjE4",
    base_url = "https://generativelanguage.googleapis.com/v1beta/"
)

# Vector Embedding
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = QdrantVectorStore.from_existing_collection(
    url = "http://localhost:6333",
    collection_name = "BhagvadGita",
    embedding = embeddings
)

#task user input
user_query = input("Ask something: ")

search_results = vector_db.similarity_search(query=user_query)

context = "\n\n".join([
                    f"Page Content : {result.page_content}\n"
                    f"Page number: {result.metadata['page_label']}\n"
                    f"File Location: {result.metadata['source']}"
                    for result in search_results])

SYSTEM_PROMPT=SYSTEM_PROMPT = f"""
You are a helpful AI assistant who answers user query based on the available context retrieved from a PDF file along with page contents and page number.

You should only answer the user based on the following Context and guide the user to open the right page number to know more.

Context:
{context}
"""

response = openai_client.chat.completions.create(
    model ="gemini-2.5-flash",
    messages= [
        { "role" : "system", "content" : SYSTEM_PROMPT},
        {"role" : "user", "content" : user_query}
    ]
)

print(f"🤖 : {response.choices[0].message.content}")