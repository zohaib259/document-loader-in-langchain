from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("catBoost.pdf")

docs = loader.load()
print(docs[1].metadata)

"""
Do not use pypdf in these 3 main scenarios:

Scanned PDFs or Images: It has no OCR. If the text is inside an image or scanned page, it returns empty text or gibberish.

Multi-Column Layouts (e.g., Papers, Magazines): It reads straight across the page horizontally, merging text from left and right columns into messy, unreadable sentences.

Complex Tables: It flattens tables into plain text, destroying the row-and-column structure needed for data/financial analysis.

Quick Alternatives
For Scanned PDFs: Use OCR (e.g., PyTesseract, Unstructured, or LlamaParse).

For Tables & Complex Layouts: Use pdfplumber or layout-aware parsers.
"""