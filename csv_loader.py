from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="sample_data.csv")

documents = loader.load()

print(f"Total rows loaded: {len(documents)}\n")

print("--- FIRST ROW CONTENT ---")
print(documents[0].page_content)  # 

print("\n--- METADATA ---")
print(documents[0].metadata)      