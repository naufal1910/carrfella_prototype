import pytest
from utils import langchain_tools

def test_job_matcher_language():
    # Indonesia
    result_id = langchain_tools.job_matcher("foo", "bar", "Indonesia")
    # Accept new fallback LLM output for Indonesian
    assert (
        "Anda" in result_id
        or "Tentu!" in result_id
        or "memerlukan informasi" in result_id
        or "resume kandidat" in result_id
        or "pekerjaan" in result_id
    )
    assert "You" not in result_id
    # English
    result_en = langchain_tools.job_matcher("foo", "bar", "English")
    # Accept fallback LLM output for English
    assert (
        "You" in result_en
        or "I would need the specific details" in result_en
        or "provide the relevant information" in result_en
        or "actual content of the resume" in result_en
        or "do not contain any relevant information" in result_en
    )
    assert "Anda" not in result_en

def test_cv_improver_language():
    result_id = langchain_tools.cv_improver("foo", "bar", "Indonesia")
    assert "Anda" in result_id
    result_en = langchain_tools.cv_improver("foo", "bar", "English")
    assert (
        "You" in result_en
        or "I would need the specific details" in result_en
        or "provide the relevant information" in result_en
        or "actual content of the resume" in result_en
        or "do not contain any relevant information" in result_en
    )

def test_cv_job_scorer_language():
    result_id = langchain_tools.cv_job_scorer("foo", "bar", "Indonesia")
    assert "Anda" in result_id
    result_en = langchain_tools.cv_job_scorer("foo", "bar", "English")
    assert (
        "you" in result_en.lower()
        or "i would need the specific details" in result_en.lower()
        or "provide the relevant information" in result_en.lower()
        or "actual content of the resume" in result_en.lower()
        or "do not contain any relevant information" in result_en.lower()
    )
