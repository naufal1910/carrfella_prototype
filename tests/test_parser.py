import os
import pytest
from utils.parser import extract_text_from_pdf, ResumePDFParseError

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "resumes")

def test_extract_text_from_valid_pdf():
    sample_pdf = os.path.join(DATA_DIR, "sample_resume.pdf")
    if not os.path.exists(sample_pdf):
        pytest.skip("sample_resume.pdf not present")
    text = extract_text_from_pdf(sample_pdf)
    assert isinstance(text, str)
    assert text.strip() != ""


def test_extract_text_from_empty_pdf():
    empty_pdf = os.path.join(DATA_DIR, "empty.pdf")
    if not os.path.exists(empty_pdf):
        pytest.skip("empty.pdf not present")
    with pytest.raises(ResumePDFParseError):
        extract_text_from_pdf(empty_pdf)


import io

def test_extract_text_from_corrupt_pdf():
    # Simulate corrupt PDF with random bytes
    corrupt_bytes = io.BytesIO(b"this is not a pdf")
    with pytest.raises(ResumePDFParseError):
        extract_text_from_pdf(corrupt_bytes)
