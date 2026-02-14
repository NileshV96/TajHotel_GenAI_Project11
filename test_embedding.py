from app.ingestion.embedding import generate_embedding


vector = generate_embedding("Luxury deluxe room with sea view")
print(len(vector))  # Should print 1536