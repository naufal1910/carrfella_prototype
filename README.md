# Carrfella Prototype

Carrfella Prototype is a lightweight Streamlit application that helps job‑seekers instantly evaluate and enhance their résumé for any job description.\
Upload your CV (PDF) and drop in a job post (text, URL or PDF), and our LangChain‑powered agent (GPT‑4o‑mini) will return:

1. A detailed **match analysis**
2. **Line‑by‑line improvement** suggestions
3. A clear **fit score**

Finally, download a polished PDF report you can share with recruiters or mentors—all within 30 seconds.

## 🚀 Pre‑flight Setup

```bash
# 1. Clone the repository
git clone https://github.com/naufal1910/carrfella_prototype.git
cd carrfella_prototype

# 2. Create & activate Python virtual env
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.\.venv\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt pytest flake8 black pytest-cov streamlit-testing

# 4. Create your .env
echo "OPENAI_API_KEY=your_openai_api_key_here" > .env

# 5. (Optional) Run dev server
streamlit run app.py
```

## 📄 Usage

1. **Upload** your résumé PDF.
2. **Provide** job description via Text, URL, or PDF.
3. **Select** language (Bahasa Indonesia / English).
4. **Click** Analyze to generate insights.
5. **Download** the combined PDF report.

## 🛠️ Tech Stack

- **Streamlit** for UI
- **LangChain & OpenAI** (GPT‑4o‑mini) for AI logic
- **PyMuPDF** & **BeautifulSoup** for parsing
- **FAISS‑cpu** for in‑memory vector caching
- **FPDF** for PDF generation

## 🐳 Docker

Build and run in Docker:

```bash
docker build -t carrfella .
docker run -p 8501:8501 carrfella
```

---

*This README is aligned with the current MVP implementation and covers only in‑scope features.*

