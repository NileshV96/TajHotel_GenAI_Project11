# Correct import for LangChain 0.2.14
from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_text(text_data, chunk_size=800, overlap=150):
    """
    text_data format:
    - String: plain text to chunk, OR
    - List: [
        {
            "content": "some extracted text",
            "metadata": {...}
        }
    ]
    
    Args:
        text_data: Text string or list of dicts with "content" and "metadata"
        chunk_size: Size of each chunk (default: 800)
        overlap: Overlap between chunks (default: 150)
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap
    )

    chunks = []

    # Handle plain string input
    if isinstance(text_data, str):
        split_texts = splitter.split_text(text_data)
        return split_texts

    # Handle list of dicts with content and metadata
    for item in text_data:
        split_texts = splitter.split_text(item["content"])

        for chunk in split_texts:
            chunks.append({
                "content": chunk,
                "metadata": item["metadata"]
            })

    return chunks
