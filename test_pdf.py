from app.ingestion.pdf_parser import extract_text_from_pdf

data = extract_text_from_pdf("data/Taj_Hotel_Details.pdf")
print(len(data))
print(data[5])