from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('/Users/shubham/Desktop/lanchain_models/text_splitter/dl-curriculum.pdf')
docs = loader.load()
splitter = CharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap = 0,
    separator=''
)
res = splitter.split_documents(docs)
print(len(res))