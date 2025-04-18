import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv()
MODEL_NAME = "gpt-4o-mini"
MAX_TOKENS = 1024

def job_matcher_func(inputs):
    resume = inputs.get("resume_text", "")
    jobdesc = inputs.get("jobdesc_text", "")
    lang = inputs.get("lang", "Indonesia")
    lang_instruction = (
        "Please provide your response in Bahasa Indonesia." if lang == "Indonesia" else "Please provide your response in English."
    )
    _prompt = f"""
    You are a career advisor AI assistant.
    Your job is to analyze a resume against a job description.
    First, extract and present the candidate's basic biodata clearly at the top, including:
    - Full Name
    - Email
    - Phone Number (if available)
    - Location (if mentioned)
    - Latest Degree
    - Most Recent Job Title
    Then, continue with:
    1. A bullet-point summary of how the resume matches or aligns with the job description.
    2. Any hidden strengths or transferable skills that might be useful for the role, even if not explicitly stated.
    {lang_instruction}
    Resume:
    {resume}
    Job Description:
    {jobdesc}
    """
    print(f"[job_matcher_func] Prompt built for lang={lang}")
    try:
        llm = ChatOpenAI(
            model_name=MODEL_NAME,
            temperature=0.4,
            max_tokens=MAX_TOKENS,
            openai_api_key=os.getenv("OPENAI_API_KEY"),
        )
        response = llm.invoke([HumanMessage(content=_prompt)])
        return response.content
    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"[ERROR] {e}"

def cv_improver_func(inputs):
    resume = inputs.get("resume_text", "")
    jobdesc = inputs.get("jobdesc_text", "")
    lang = inputs.get("lang", "Indonesia")
    lang_instruction = (
        "Please provide your response in Bahasa Indonesia." if lang == "Indonesia" else "Please provide your response in English."
    )
    _prompt = f"""
    You are an expert CV reviewer. Analyze the following resume and job description, and provide:
    1. A bullet-list of the most important improvements to make the resume better fit the job.
    2. Suggestions for additional skills or experiences to highlight.
    {lang_instruction}
    Resume:
    {resume}
    Job Description:
    {jobdesc}
    """
    print(f"[cv_improver_func] Prompt built for lang={lang}")
    try:
        llm = ChatOpenAI(
            model_name=MODEL_NAME,
            temperature=0.4,
            max_tokens=MAX_TOKENS,
            openai_api_key=os.getenv("OPENAI_API_KEY"),
        )
        response = llm.invoke([HumanMessage(content=_prompt)])
        return response.content
    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"[ERROR] {e}"

def cv_job_scorer_func(inputs):
    resume = inputs.get("resume_text", "")
    jobdesc = inputs.get("jobdesc_text", "")
    lang = inputs.get("lang", "Indonesia")
    lang_instruction = (
        "Please provide your response in Bahasa Indonesia." if lang == "Indonesia" else "Please provide your response in English."
    )
    _prompt = f"""
    You are a job fit scoring assistant. Review the resume and job description and return:
    1. A numeric fit score out of 100.
    2. A 1-2 sentence justification for the score.
    {lang_instruction}
    Resume:
    {resume}
    Job Description:
    {jobdesc}
    """
    print(f"[cv_job_scorer_func] Prompt built for lang={lang}")
    try:
        llm = ChatOpenAI(
            model_name=MODEL_NAME,
            temperature=0.4,
            max_tokens=MAX_TOKENS,
            openai_api_key=os.getenv("OPENAI_API_KEY"),
        )
        response = llm.invoke([HumanMessage(content=_prompt)])
        return response.content
    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"[ERROR] {e}"

def job_matcher(resume_text, jobdesc_text, lang):
    return job_matcher_func({"resume_text": resume_text, "jobdesc_text": jobdesc_text, "lang": lang})

def cv_improver(resume_text, jobdesc_text, lang):
    return cv_improver_func({"resume_text": resume_text, "jobdesc_text": jobdesc_text, "lang": lang})

def cv_job_scorer(resume_text, jobdesc_text, lang):
    return cv_job_scorer_func({"resume_text": resume_text, "jobdesc_text": jobdesc_text, "lang": lang})
