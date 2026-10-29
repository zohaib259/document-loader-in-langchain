"""
it is used to load the multiple documents form the directory
"""

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

# Use the absolute path directly without './'
folder_path = r"C:\Users\zohai\OneDrive\Desktop\ML books"

loader = DirectoryLoader(
    folder_path,
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

print("Loading PDF books...")
docs = loader.lazy_load()

for documents in docs:
    print(documents.metadata)