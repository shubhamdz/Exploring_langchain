from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('/Users/shubham/Desktop/lanchain_models/data_loader/dl-curriculum.pdf')

docs  = loader.load()

print(len(docs))

print(docs[0])

print(docs[0].page_content)
print(docs[0].metadata)