from app.ingestion.pdf_parser import extract_text_from_pdf
from app.ingestion.chunking import chunk_text
from app.ingestion.embedding import generate_embedding
from app.db.connections import get_connection
from sqlalchemy import text
import json

def run_ingestion():
    conn = get_connection()

    pdf_data = extract_text_from_pdf("data/Taj_Hotel_Details.pdf")
    chunks = chunk_text(pdf_data)

    for chunk in chunks:
        # Insert document
        result = conn.execute(
            text("INSERT INTO documents (content, metadata) VALUES (:content, :metadata) RETURNING id"),
            {"content": chunk["content"], "metadata": json.dumps(chunk["metadata"])}
        )

        doc_id = result.fetchone()[0]

        # Generate embedding
        embedding = generate_embedding(chunk["content"])

        # Insert embedding
        conn.execute(
            text("INSERT INTO embeddings (document_id, embedding) VALUES (:doc_id, :embedding)"),
            {"doc_id": doc_id, "embedding": embedding}
        )

    conn.commit()
    conn.close()

if __name__ == "__main__":
    run_ingestion()
