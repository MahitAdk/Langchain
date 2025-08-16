from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')#Download file from campusx github account later on

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)

#Pypdf is not able to extract text from scanned images in pdfs and we use amazon textract for that and unstructured for table