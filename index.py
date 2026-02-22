# from dotenv import load_dotenv
# load_dotenv()

from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore

pdf_path = Path(__file__).parent / "The Bhagavad Gita.pdf"
loader = PyPDFLoader(file_path=pdf_path)

# splitting the pdf into documents(pages)
docs = loader.load()

# every page is a document in that pdf file
# print(docs[32])  #you can print the page numbers, which will the nth document that is printed

#splitting the document into texts
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
chunks = text_splitter.split_documents(documents=docs)

#LangChain even gives a utility to create vector embeddings from chunks
#VECTOR EMBEDDING
# embeddings = GoogleGenerativeAIEmbeddings(model="text-embedding-004")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

#Vector db
vector_store = QdrantVectorStore.from_documents(
    documents = chunks,
    embedding = embeddings,
    url = "http://localhost:6333",
    collection_name = "BhagvadGita"
)

print("Vector embeddings are created.Indexing of docs done")


