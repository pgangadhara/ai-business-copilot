from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict

import faiss
from sentence_transformers import SentenceTransformer


@dataclass
class RetrievalChunk:
    text: str
    source: str


class VectorStore:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.chunks: List[RetrievalChunk] = []

    def add(self, text: str, source: str) -> None:
        cleaned = text.strip()
        if cleaned:
            self.chunks.append(RetrievalChunk(text=cleaned, source=source))

    def build(self) -> None:
        texts = [c.text for c in self.chunks]
        embeddings = self.model.encode(texts, show_progress_bar=False)
        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)

    def search(self, query: str, k: int = 3) -> List[Dict]:
        if self.index is None:
            raise RuntimeError("Vector index not built. Call build() first.")

        q_emb = self.model.encode([query])
        _, idxs = self.index.search(q_emb, k)

        results = []
        for i in idxs[0]:
            chunk = self.chunks[int(i)]
            results.append({"source": chunk.source, "text": chunk.text})
        return results


def load_policy_docs(docs_dir: Path) -> VectorStore:
    store = VectorStore()

    for md_file in docs_dir.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        store.add(content, source=md_file.name)

    store.build()
    return store
