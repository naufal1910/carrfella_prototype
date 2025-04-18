import time

def job_matcher(resume_text, jobdesc_text, lang):
    # Simulate tool call
    print(f"[job_matcher] called with lang={lang}")
    time.sleep(0.5)
    return f"Job match result for lang={lang}"

def cv_improver(resume_text, jobdesc_text, lang):
    print(f"[cv_improver] called with lang={lang}")
    time.sleep(0.5)
    return f"CV improvement suggestions for lang={lang}"

def cv_job_scorer(resume_text, jobdesc_text, lang):
    print(f"[cv_job_scorer] called with lang={lang}")
    time.sleep(0.5)
    return f"Job score for lang={lang}: 85/100"
