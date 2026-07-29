📘 GitaInsight Engine – LLM-Powered Question Answering on the Bhagavad Gita

GitaInsight is a Retrieval-Augmented Generation (RAG) based Question Answering system built on the Bhagavad Gita.

The system converts the Gita PDF into semantic chunks, generates vector embeddings using Hugging Face models, stores them in a vector database (Dockerized), and retrieves relevant passages to answer user queries using the Gemini LLM.


🚀 Project Overview

This project demonstrates:

📄 PDF Processing & Chunking

🧠 Vector Embeddings using Hugging Face

🗄️ Vector Database (Docker Container)

🔎 Semantic Similarity Search

🤖 LLM-based Answer Generation (Gemini)

🐳 Containerized Deployment using Docker


It follows the RAG (Retrieval-Augmented Generation) architecture.


🏗️ System Architecture

User Query

⬇

Convert Query → Vector Embedding

⬇

Similarity Search in Vector DB

⬇

Retrieve Top-K Relevant Chunks

⬇

Pass Context + Query to Gemini LLM

⬇

Generated Answer


🧠 Tech Stack

Language: Python

Embedding Model: Hugging Face Sentence Transformers

LLM: Gemini

Vector Database: Chromadb

Containerization: Docker


⚙️ How It Works
1️⃣ PDF Ingestion

Load the Bhagavad Gita PDF

Extract text

Split text into semantic chunks

2️⃣ Embedding Generation

Use Hugging Face embedding model

Convert chunks into high-dimensional vectors

3️⃣ Vector Storage

Store embeddings in a Dockerized vector database

Enable fast similarity search

4️⃣ Query Processing

Convert user query into embedding

Perform cosine similarity search

Retrieve top relevant chunks

5️⃣ Answer Generation

Pass retrieved chunks + query to Gemini LLM

Generate context-aware answer

🐳 Running with Docker
Step 1: Start Vector Database
docker-compose up -d
Step 2: Install Dependencies
pip install -r requirements.txt
Step 3: Run Application
python main.py
📝 Example Query
What does Krishna say about karma?

The system:

Finds relevant verses

Sends context to Gemini

Generates a structured answer


🎯 Key Features

Semantic Search (not keyword-based)

Context-aware LLM answers

Scalable vector database

Fully containerized setup

Clean RAG pipeline implementation


📊 Future Improvements

Add Web UI (Streamlit / FastAPI)

Add Verse Citation in responses

Add Multiple Scriptural Support

Deploy on Cloud

Add Hybrid Search (BM25 + Vector)

📚 Learning Outcomes

Practical implementation of RAG architecture

Understanding embeddings & vector similarity

Docker container orchestration

Integrating Hugging Face + Gemini LLM
