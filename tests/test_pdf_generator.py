from utils.pdf_generator import generate_pdf

def test_generate_pdf_size():
    match = "Match Analysis\n" + ("A" * 1000)
    improve = "CV Improvement Suggestions\n" + ("B" * 1000)
    score = "Fit Score\n" + ("C" * 1000)
    pdf_bytes = generate_pdf(match, improve, score)
    # Should be >5kB
    assert isinstance(pdf_bytes, bytes)
    assert len(pdf_bytes) > 5120
