from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path = '/Users/shubham/Desktop/lanchain_models/data_loader/books',
    glob = "*.pdf",
    loader_cls = PyPDFLoader
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)

