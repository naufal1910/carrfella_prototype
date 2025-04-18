import pytest
from utils import langchain_tools

def test_job_matcher_language():
    # Indonesia
    result_id = langchain_tools.job_matcher("foo", "bar", "Indonesia")
    assert "Anda" in result_id
    assert "You" not in result_id
    # English
    result_en = langchain_tools.job_matcher("foo", "bar", "English")
    assert "You" in result_en
    assert "Anda" not in result_en

def test_cv_improver_language():
    result_id = langchain_tools.cv_improver("foo", "bar", "Indonesia")
    assert "Anda" in result_id
    result_en = langchain_tools.cv_improver("foo", "bar", "English")
    assert "You" in result_en

def test_cv_job_scorer_language():
    result_id = langchain_tools.cv_job_scorer("foo", "bar", "Indonesia")
    assert "Anda" in result_id
    result_en = langchain_tools.cv_job_scorer("foo", "bar", "English")
    assert "you" in result_en.lower()
