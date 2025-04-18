from streamlit.testing.v1 import AppTest


def test_app_smoke():
    at = AppTest.from_file("app.py")
    at.run()
    # Check title
    assert at.title[0].value == "Career Agent Advisor"
    # Check all four headers
    headers = [h.value for h in at.header]
    assert "1. Résumé PDF Upload" in headers
    assert "2. Job Description Input" in headers
    assert "3. Language Selector" in headers
    assert "4. Analyse" in headers
    # Check Analyse button exists
    assert at.button["analyse_btn"].label == "Analyse"
    # Click Analyse and check for log
    at.button["analyse_btn"].click()
    assert any(
        "Analyse clicked" in m.value
        for m in at.markdown + at.text + at.write
    )
