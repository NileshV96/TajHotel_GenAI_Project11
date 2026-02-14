from app.db.connections import get_connection
from app.embeddings.embedder import get_embedding
from sqlalchemy import text, bindparam, String, Integer


def retrieve_similar_chunks(query: str, top_k: int = 3):
    conn = get_connection()

    query_embedding = get_embedding(query)
    # Convert embedding list to pgvector format string
    embedding_str = "[" + ",".join(str(x) for x in query_embedding) + "]"

    result = conn.execute(
        text("""
            SELECT content
            FROM embeddings
            ORDER BY embedding <-> CAST(:embedding AS vector)
            LIMIT :top_k;
        """).bindparams(
            bindparam("embedding", type_=String),
            bindparam("top_k", type_=Integer)
        ),
        {"embedding": embedding_str, "top_k": top_k}
    )

    results = result.fetchall()

    conn.close()

    return [row[0] for row in results]
