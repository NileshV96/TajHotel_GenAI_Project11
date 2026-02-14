from app.ingestion.chunking import chunk_text

# Sample text for testing
sample_text = """
Welcome to Paradise Hotel.
We offer luxury rooms with sea view.
Our pricing varies by season.
Deluxe Room - ₹5000 per night.
Suite Room - ₹9000 per night.
Breakfast included.
Free WiFi available.
Swimming pool and spa services.
""" * 10  # repeat to make text bigger


chunks = chunk_text(sample_text, chunk_size=200, overlap=50)

print(f"Total Chunks Created: {len(chunks)}")
print("\n---- First Chunk ----\n")
print(chunks[0])
print("\n---- Second Chunk ----\n")
print(chunks[1])
