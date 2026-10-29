from langchain_community.document_loaders import TextLoader

# 1. Initialize the TextLoader with the path to your file
# (Ensure 'sample_document.txt' is in the same folder as this script)
loader = TextLoader("some_text.txt", encoding="utf-8")

# 2. Load the document into a list of Document objects
documents = loader.load()

# 3. Inspect the loaded document
print(f"Total documents loaded: {len(documents)}\n")

# Print the metadata (LangChain automatically extracts file paths)
print("--- METADATA ---")
print(documents[0].metadata)

# Print a preview of the page content
print("\n--- PAGE CONTENT PREVIEW ---")
print(documents[0].page_content[:400])  # prints the first 400 characters