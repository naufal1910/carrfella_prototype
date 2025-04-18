import fitz  # PyMuPDF


class ResumePDFParseError(Exception):
    """Raised when a PDF is corrupt or contains no extractable text."""
    pass


def extract_text_from_pdf(file):
    try:
        if hasattr(file, "read"):
            file.seek(0)
            pdf_bytes = file.read()
        else:
            with open(file, "rb") as f:
                pdf_bytes = f.read()
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        text = " ".join(page.get_text() for page in doc)
        doc.close()
        if not text.strip():
            raise ResumePDFParseError("No extractable text in PDF.")
        return text
    except Exception as e:
        raise ResumePDFParseError(f"Could not parse PDF: {e}")
