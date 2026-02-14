import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text_data = []

    for page_number, page in enumerate(doc):
        text = page.get_text()
        text_data.append({
            "content": text,
            "metadata": {"page": page_number}
        })

    return text_data
