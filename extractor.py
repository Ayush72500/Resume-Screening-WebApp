"""
extractor.py

Handles PDF text extraction using the pypdf library.
Provides a clean, reusable function to extract text safely from uploaded PDF files.
"""

import pypdf


def extract_text_from_pdf(pdf_file) -> str:
    """
    Extracts text from a given PDF file object or file path.

    Parameters:
        pdf_file: File-like object (e.g. BytesIO from Streamlit uploader) or file path string.

    Returns:
        str: Cleaned extracted text, or an empty string if text cannot be extracted.
    """
    if pdf_file is None:
        return ""

    try:
        reader = pypdf.PdfReader(pdf_file)
        extracted_pages = []

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                extracted_pages.append(page_text)

        full_text = "\n".join(extracted_pages).strip()
        return full_text

    except Exception as e:
        # Log or handle unreadable / corrupted PDF gracefully
        print(f"Error extracting text from PDF: {e}")
        return ""
