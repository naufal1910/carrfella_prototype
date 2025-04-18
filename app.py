import streamlit as st

def main():
    st.set_page_config(page_title="Career Agent Advisor")
    st.title("Career Agent Advisor")

    # Résumé PDF uploader
    st.header("1. Résumé PDF Upload")
    st.file_uploader(
        "Upload your résumé (PDF only)",
        type=["pdf"],
        key="resume_pdf",
    )

    # Job Description Input
    st.header("2. Job Description Input")
    job_input_mode = st.radio(
        "How would you like to provide the job description?",
        ("Paste Text", "Job URL", "Upload PDF"),
        key="job_input_mode",
    )
    job_text_val = None
    job_url_val = None
    job_pdf_val = None
    if job_input_mode == "Paste Text":
        job_text_val = st.text_area(
            "Paste the job description here",
            key="job_text",
        )
    elif job_input_mode == "Job URL":
        job_url_val = st.text_input(
            "Enter the job posting URL",
            key="job_url",
        )
    elif job_input_mode == "Upload PDF":
        job_pdf_val = st.file_uploader(
            "Upload job description PDF",
            type=["pdf"],
            key="job_pdf",
        )

    # Language Selector
    st.header("3. Language Selector")
    st.selectbox(
        "Select language",
        ("Indonesia", "English"),
        key="lang_select",
    )

    # Analyse Button
    st.header("4. Analyse")
    if st.button("Analyse", key="analyse_btn"):
        # --- JOB DESCRIPTION EXTRACTION LOGIC ---
        from utils.parser import extract_text_from_url, extract_text_from_pdf, ResumeJobDescParseError, ResumePDFParseError
        job_desc_text = None
        error_msg = None
        try:
            if job_input_mode == "Paste Text":
                if not job_text_val or len(job_text_val.strip()) < 200:
                    raise ResumeJobDescParseError("Please paste at least 200 characters of job description text.")
                job_desc_text = job_text_val.strip()
            elif job_input_mode == "Job URL":
                if not job_url_val or not job_url_val.strip():
                    raise ResumeJobDescParseError("Please enter a valid job posting URL.")
                job_desc_text = extract_text_from_url(job_url_val.strip())
            elif job_input_mode == "Upload PDF":
                if not job_pdf_val:
                    raise ResumePDFParseError("Please upload a job description PDF file.")
                job_desc_text = extract_text_from_pdf(job_pdf_val)
                if not job_desc_text or len(job_desc_text.strip()) < 200:
                    raise ResumeJobDescParseError("Extracted job description from PDF is too short.")
            # If we get here, job_desc_text is valid
            st.success("Job description extracted successfully!")
            st.write(job_desc_text)
        except (ResumeJobDescParseError, ResumePDFParseError) as e:
            st.error(str(e))
        except Exception as e:
            st.error(f"Unexpected error: {e}")
  # Stub callback


if __name__ == "__main__":
    main()
