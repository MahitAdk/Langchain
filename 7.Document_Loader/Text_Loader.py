from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI()

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader=TextLoader('cricket.txt', encoding='utf-8')#uft-8 indicates the encoding format and that there are no special characters in the text file

data=loader.load()

print(data[0].page_content)  # Print the content of the first document
print(data[0].metadata)  # Print the metadata of the first document


chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))