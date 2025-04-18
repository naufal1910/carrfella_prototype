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
    if job_input_mode == "Paste Text":
        st.text_area(
            "Paste the job description here",
            key="job_text",
        )
    elif job_input_mode == "Job URL":
        st.text_input(
            "Enter the job posting URL",
            key="job_url",
        )
    elif job_input_mode == "Upload PDF":
        st.file_uploader(
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
        st.write("Analyse clicked")  # Stub callback


if __name__ == "__main__":
    main()
