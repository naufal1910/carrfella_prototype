import fitz  # PyMuPDF
import requests
from bs4 import BeautifulSoup


class ResumeJobDescParseError(Exception):
    """Raised when a job description cannot be extracted or is too short."""
    pass


class ResumePDFParseError(ResumeJobDescParseError):
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


def extract_text_from_url(url):
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        # Heuristic: get visible text, ignoring script/style
        for tag in soup(["script", "style", "noscript"]):
            tag.extract()
        text = " ".join(soup.stripped_strings)
        if not text or len(text) < 200:
            raise ResumeJobDescParseError(
                "Extracted job description is too short or empty."
            )
        return text
    except Exception as e:
        raise ResumeJobDescParseError(f"Could not extract job description from URL: {e}")
