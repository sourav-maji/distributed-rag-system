# FastAPI RAG with Redis Queue (RQ)

A **distributed Retrieval-Augmented Generation (RAG)** system built using **FastAPI**, **LangChain**, **Qdrant**, and **Redis Queue (RQ)**.

This project demonstrates how to handle RAG queries asynchronously using a background worker, making it scalable and production-ready.

---

## 🚀 Features

- PDF document ingestion and vector indexing
- Semantic search using Qdrant
- Asynchronous query processing with Redis Queue (RQ)
- FastAPI-based REST API
- Background workers for retrieval & generation
- Clean, modular architecture

---

## 🧱 Tech Stack

- **Python 3.9+**
- **FastAPI**
- **LangChain**
- **Qdrant (Vector Database)**
- **Redis + RQ**
- **OpenAI Embeddings**
- **Docker**

---

## 📂 Project Structure

```bash
rag_queue/
├── client/
│   └── rq_client.py        # Redis + RQ configuration
├── queues/
│   └── worker.py           # RAG worker (retrieval + generation)
├── server.py               # FastAPI app
├── main.py                 # Entry point
├── index.py                # PDF ingestion & vector indexing
├── retrieve.py             # Local retrieval testing
├── requirements.txt
├── .env                    # API keys (ignored)
├── README.md
└── data/
    └── sample.pdf
