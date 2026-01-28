# AI Business Copilot

A Python-based AI system that analyzes business data, generates KPI reports,
and provides policy-grounded answers using Retrieval-Augmented Generation (RAG).

## Features
- Automated KPI analysis and markdown report generation
- AI-style executive summary grounded in internal policies
- RAG pipeline using SentenceTransformers and FAISS
- FastAPI service exposing policy-grounded Q&A

## Project Structure

## API Documentation (Swagger UI)

The FastAPI service exposes interactive API documentation via Swagger UI.

To view it locally:
```bash
python -m uvicorn app.api:app --reload

