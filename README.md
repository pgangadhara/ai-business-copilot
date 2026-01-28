# AI Business Copilot

A production-style **Python AI system** that analyzes business data, generates KPI reports, and delivers **policy‑grounded answers** using **Retrieval‑Augmented Generation (RAG)**. The project emphasizes **auditability, reproducibility, and enterprise‑ready design**.

---

## 🚀 What This Project Demonstrates

* End‑to‑end analytics → AI → API workflow
* Deterministic KPI computation with versioned outputs
* Grounded AI (no hallucinations) via RAG over internal policies
* FastAPI service with interactive Swagger documentation
* Clean repo hygiene and reproducible setup

---

## ✨ Features

* **Automated KPI Analysis**: Processes structured sales data and produces a markdown KPI report
* **AI Executive Summary**: Generates an executive‑style summary grounded in internal policy documents
* **RAG Pipeline**: Uses SentenceTransformers + FAISS for citation‑backed answers
* **FastAPI Service**: Exposes health checks and policy‑grounded Q&A endpoints
* **Visible Artifacts**: Reports are committed so reviewers can evaluate outputs without running code

---

## 📂 Project Structure

```
app/
  analyze.py            # KPI computation and report generation
  insights.py           # AI-style executive summary
  vector_store.py       # Embeddings + FAISS vector index
  rag.py                # Retrieval-Augmented Generation logic
  run_rag_demo.py       # Generates example RAG outputs
  api.py                # FastAPI service

data/
  sales_sample.csv      # Sample sales dataset

docs/
  pricing_policy.md     # Business pricing policy
  refund_policy.md      # Business refund policy
  swagger_ui.png        # Swagger UI screenshot (static preview)

reports/
  analysis_report.md    # KPI report output
  ai_executive_summary.md
  rag_demo.md           # RAG demo with cited answers

requirements.txt
README.md
```

---

## 📊 Outputs (Start Here)

👉 **Quickest way to understand value**: open the files below directly on GitHub.

* `reports/analysis_report.md` — KPI metrics and trends
* `reports/ai_executive_summary.md` — Policy‑grounded executive summary
* `reports/rag_demo.md` — Citation‑backed RAG answers

---

## 🧠 RAG Overview (High Level)

1. Policy documents are embedded using **SentenceTransformers**
2. Embeddings are indexed with **FAISS** for fast similarity search
3. User questions retrieve the most relevant policy context
4. Answers are generated **only from retrieved context**, ensuring grounding

---

## 🌐 API Documentation (FastAPI + Swagger UI)

The project exposes a REST API for policy‑grounded Q&A.

### Run the API locally

```bash
pip install -r requirements.txt
python -m uvicorn app.api:app --reload
```

### Open Swagger UI

Once the server is running, open:

```
http://127.0.0.1:8000/docs
```

### Available Endpoints

* `GET /health` — Service health check
* `POST /ask` — Policy‑grounded question answering (RAG)

### Swagger UI Preview

![Swagger UI](docs/swagger_ui.png)

---

## ▶️ How to Run End‑to‑End

```bash
# 1. Generate KPI report
python app/analyze.py

# 2. Generate AI executive summary
python app/insights.py

# 3. Generate RAG demo outputs
python app/run_rag_demo.py

# 4. Start API
python -m uvicorn app.api:app --reload
```

---

## 🧪 Example API Request

```json
{
  "question": "Are discounts allowed on hardware products?"
}
```

The response includes retrieved policy context and a grounded answer.

---

## 🏗️ Design Principles

* **Grounded AI**: No free‑form generation without retrieved evidence
* **Reproducibility**: Deterministic outputs committed to the repo
* **Separation of Concerns**: Analytics, RAG, and API layers are isolated
* **Enterprise Readiness**: Clear structure, documentation, and hygiene

---

## 📌 Notes

* Swagger UI (`/docs`) is generated dynamically by FastAPI and runs locally
* GitHub hosts **static artifacts and screenshots**, not live services

---

## 📄 License

MIT
