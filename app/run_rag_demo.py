from pathlib import Path
from rag import rag_answer

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent
    out_path = base_dir / "reports" / "rag_demo.md"

    questions = [
        "Are discounts allowed on hardware products?",
        "What is the refund eligibility window?",
        "Are service engagements refundable after delivery starts?"
    ]

    lines = ["# RAG Demo Output\n\n"]
    for q in questions:
        lines.append(rag_answer(q))
        lines.append("\n---\n\n")

    out_path.write_text("".join(lines), encoding="utf-8")
    print("✅ RAG demo written to:", out_path)
