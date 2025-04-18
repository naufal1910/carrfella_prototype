def test_extract_text_from_url_happy():
    from unittest import mock
    html = """
    <html><body>
    <div>Job Title</div>
    <p>{}</p>
    </body></html>
    """.format("A" * 210)
    with mock.patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = html
        from utils.parser import extract_text_from_url
        result = extract_text_from_url("http://example.com/job")
        assert "Job Title" in result
        assert len(result) >= 200

def test_extract_text_from_url_invalid_url():
    from unittest import mock
    with mock.patch("requests.get", side_effect=Exception("Bad URL")):
        from utils.parser import extract_text_from_url, ResumeJobDescParseError
        import pytest
        with pytest.raises(ResumeJobDescParseError):
            extract_text_from_url("http://badurl")

def test_extract_text_from_url_short_text():
    from unittest import mock
    html = "<html><body><p>Short</p></body></html>"
    with mock.patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = html
        from utils.parser import extract_text_from_url, ResumeJobDescParseError
        import pytest
        with pytest.raises(ResumeJobDescParseError):
            extract_text_from_url("http://example.com/short")
