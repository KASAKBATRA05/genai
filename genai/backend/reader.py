
import fitz
def extract_text_from_pdf(f):
    doc = fitz.open(stream=f.read(), filetype="pdf")
    return " ".join(page.get_text() for page in doc)
def extract_text_from_txt(f):
    return f.read().decode()
