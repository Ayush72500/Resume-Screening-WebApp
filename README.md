# 📄 Resume Screening & Role Classification System

A lightweight, fast, and automated **Python + Streamlit** web application that parses PDF resumes and classifies candidates against industry job roles using intelligent skill matching algorithms.

---

## 📌 What is this Project?

This application simplifies candidate resume evaluation. When a user uploads a PDF resume, the system automatically:

1. Extracts and cleans the text from the PDF.
2. Scans for key technical and professional skills using precise regex matching.
3. Classifies the resume into the best-fit job role based on candidate skillset and keyword density.
4. Immediately purges temporary files to maintain security and storage efficiency.

---

## ✨ Key Features

- 📄 **PDF Text Parser**: Fast & safe text extraction powered by `pypdf`.
- 🎯 **Smart Keyword Matching**: Case-insensitive regex matching with word boundaries to prevent false positive matches.
- 📊 **Multi-Role Classification**: Dynamically matches candidate profiles across key industry roles (Software Engineering, Data Science, Cloud/DevOps, Analytics, HR, Business Development, and more).
- 🧹 **Auto Cleanup**: Temporary uploaded files are automatically deleted after text extraction.
- ⚡ **Clean Streamlit UI**: Fast, responsive, clutter-free user interface.

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/resume-screening.git
cd resume-screening
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```

Open **http://localhost:8501** in your browser.

---

## 📁 Project Structure

```text
├── app.py           # Streamlit Web UI & main execution flow
├── analyzer.py      # Core text cleaning & role matching logic
├── extractor.py     # PDF text extraction module
├── roles.py         # Dictionary of target job roles and skill keywords
├── utils.py         # File management & temporary cleanup utilities
├── requirements.txt # Project dependencies (streamlit, pypdf)
└── README.md        # Project documentation
```

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Streamlit** (Frontend UI)
- **pypdf** (PDF Text Extraction)
