"""this work well on static websites"""
from langchain_community.document_loaders import WebBaseLoader

# 1. Provide the URL(s) you want to load
loader = WebBaseLoader("https://docs.python.org/3/")

# 2. Load the web page contents into Document objects
docs = loader.load()

print(f"Total documents loaded: {len(docs)}")
print("\n--- METADATA ---")
print(docs[0].metadata)  # Shows source URL, title, description, etc.

print("\n--- CONTENT PREVIEW ---")
print(docs[0].page_content[:300])  # Prints the first 300 characters of scraped text