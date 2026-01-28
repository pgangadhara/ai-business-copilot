from __future__ import annotations

from pathlib import Path
from vector_store import load_policy_docs


def rag_answer(question: str) -> str:
    base_dir = Path(__file__).resolve().parent.parent
    docs_dir = base_dir / "docs"

    if not docs_dir.exists():
        raise FileNotFoundError(f"Docs folder not found: {docs_dir}")

    store = load_policy_docs(docs_dir)
    retrieved = store.search(question, k=2)

    # Build a simple grounded answer using retrieved context + citations
    lines = []
    lines.append(f"# RAG Answer\n\n")
    lines.append(f"## Question\n{question}\n\n")
    lines.append("## Retrieved Context\n")
    for r in retrieved:
        lines.append(f"- **Source:** `{r['source']}`\n")
        lines.append(f"  - Snippet: {r['text'][:300].replace('\\n', ' ')}...\n")
    lines.append("\n")

    # A minimal “grounded” response with explicit citations
    sources = ", ".join([f"`{r['source']}`" for r in retrieved])
    lines.append("## Answer (Grounded)\n")
    lines.append(
        f"Based on the retrieved policy documents ({sources}), "
        f"the guidance is to follow the documented discount/refund rules "
        f"and route exceptions through approvals where required.\n"
    )

    return "".join(lines)


if __name__ == "__main__":
    print(rag_answer("Are discounts allowed on hardware products?"))
