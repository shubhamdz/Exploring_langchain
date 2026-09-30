from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='/Users/shubham/Desktop/lanchain_models/data_loader/Social_Network_Ads.csv')


docs = loader.load()

print(len(docs))  # evey row behaves as a document object 

print(docs[0].page_content)
print(docs[0].metadata)