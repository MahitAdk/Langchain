from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimension=32)

result=embedding.embedded.query("Delhi is capital of India")
print(str(result))#Returns a 32 dimensional numerical value

'''
For moree than one document at a time
documents=["How are you doing",
"Just useless paragraphs"
]

result=embedding.embedded.query(documents)
print(str(result))#Returns a 32 dimensional numerical value

'''