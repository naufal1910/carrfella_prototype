from fpdf import FPDF

def generate_pdf(match, improve, score):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", "B", 16)
    # Section 1
    pdf.cell(0, 10, "Match Analysis", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, match)
    pdf.ln(5)
    # Section 2
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "CV Improvement Suggestions", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, improve)
    pdf.ln(5)
    # Section 3
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Fit Score", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, score)
    # Output as bytes
    pdf_bytes = pdf.output(dest="S").encode("utf-8")
    return pdf_bytes
