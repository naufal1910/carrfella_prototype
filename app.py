import streamlit as st

def main():
    st.set_page_config(page_title="Career Agent Advisor")
    st.title("Career Agent Advisor")

    # Résumé PDF uploader
    st.header("1. Résumé PDF Upload")
    resume_pdf_val = st.file_uploader(
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
    lang_val = st.selectbox(
        "Select language",
        ("Indonesia", "English"),
        key="lang_select",
        index=0  # Default to 'Indonesia'
    )

    # Analyse Button
    st.header("4. Analyse")
    if st.button("Analyse", key="analyse_btn"):
        import time
        from utils.parser import extract_text_from_url, extract_text_from_pdf, ResumeJobDescParseError, ResumePDFParseError
        from utils.langchain_tools import job_matcher, cv_improver, cv_job_scorer
        job_desc_text = None
        resume_text = None
        try:
            # --- JOB DESCRIPTION EXTRACTION ---
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

            # --- RÉSUMÉ EXTRACTION ---
            if not resume_pdf_val:
                raise ResumePDFParseError("Please upload a résumé PDF file.")
            resume_text = extract_text_from_pdf(resume_pdf_val)
            if not resume_text or len(resume_text.strip()) < 200:
                raise ResumePDFParseError("Extracted résumé text is too short.")

            # --- LANGCHAIN TOOLS SEQUENTIAL CALLS ---
            st.info("Invoking analysis tools...")
            results = {}
            timings = {}
            for tool_name, tool_fn in [
                ("job_matcher", job_matcher),
                ("cv_improver", cv_improver),
                ("cv_job_scorer", cv_job_scorer),
            ]:
                start = time.perf_counter()
                result = tool_fn(resume_text, job_desc_text, lang_val)
                duration = time.perf_counter() - start
                print(f"[{tool_name}] took {duration:.2f}s")
                results[tool_name] = result
                timings[tool_name] = duration
            st.success("Analysis complete!")
            # Chat bubbles for each result
            chat_labels = [
                ("Match Analysis", results["job_matcher"], timings["job_matcher"]),
                ("CV Improvement Suggestions", results["cv_improver"], timings["cv_improver"]),
                ("Fit Score", results["cv_job_scorer"], timings["cv_job_scorer"]),
            ]
            for label, content, timing in chat_labels:
                with st.chat_message("assistant"):
                    st.markdown(f"**{label}:**")
                    st.write(content)
                    st.caption(f"Time: {timing:.2f}s")

            # --- Download PDF Button ---
            from utils.pdf_generator import generate_pdf
            import re
            from datetime import datetime
            pdf_bytes = generate_pdf(
                results["job_matcher"],
                results["cv_improver"],
                results["cv_job_scorer"]
            )
            # Try to extract candidate name from job_matcher result (first line or after 'Name:')
            match_text = results["job_matcher"]
            name = "career"
            name_match = re.search(r"Name\s*[:：]\s*([\w\s'.-]+)", match_text, re.IGNORECASE)
            if name_match:
                name = name_match.group(1).strip().replace(" ", "_")
            else:
                # fallback: first word in first line if looks like a name
                first_line = match_text.splitlines()[0].strip()
                if len(first_line.split()) <= 5 and all(c.isalpha() or c in " .-'" for c in first_line):
                    name = first_line.replace(" ", "_")
            nowstr = datetime.now().strftime("%y%m%d%H%M%S")
            file_name = f"{nowstr}_{name}_report.pdf"
            st.download_button(
                label="Download PDF Report",
                data=pdf_bytes,
                file_name=file_name,
                mime="application/pdf",
                disabled=(len(pdf_bytes) < 5120)
            )
        except (ResumeJobDescParseError, ResumePDFParseError) as e:
            st.error(str(e))
        except Exception as e:
            st.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
