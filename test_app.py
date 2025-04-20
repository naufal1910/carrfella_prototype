from streamlit.testing.v1 import AppTest


def test_app_smoke():
    at = AppTest.from_file("app.py")
    at.run()
    # Check title
    assert at.title[0].value == "CARRFELLA - Career Advisor Assistant"
    # Check all four headers
    headers = [h.value for h in at.header]
    assert "1. Resume PDF Upload" in headers
    assert "2. Job Description Input" in headers
    assert "3. Language Selector" in headers
    assert "4. Analyse" in headers
    # Check Analyse button exists
    assert any(btn.label == "Analyse" for btn in at.button)
    # Click Analyse and check for log
    at.button[0].click()
    print("TEXT OUTPUT:", [t.value for t in at.text])
    print("MARKDOWN OUTPUT:", [m.value for m in at.markdown])
    all_outputs = list(getattr(at, "text", [])) + list(getattr(at, "markdown", []))
    assert any(
        "Analyse clicked" in m.value
        for m in all_outputs
    )
    assert "4. Analyse" in headers
    # Check Analyse button exists
    assert any(btn.label == "Analyse" for btn in at.button)
    # Click Analyse and check for log
    at.button[0].click()
    print("TEXT OUTPUT:", [t.value for t in at.text])
    print("MARKDOWN OUTPUT:", [m.value for m in at.markdown])
    all_outputs = list(getattr(at, "text", [])) + list(getattr(at, "markdown", []))
    assert any(
        "Analyse clicked" in m.value
        for m in all_outputs
    )
