from langchain_google_genai  import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

prompt1= PromptTemplate(
    tempalte='Write a paragraph about the topic:{topic}',
    input_variables=['topic']
)

prompt2= PromptTemplate(
    tempalte='Explain the above paragraph in detail-{text}',
    input_variables=['text']
)

model=ChatGoogleGenerativeAI()

parser=StrOutputParser()

result=RunnableSequence(prompt1,model,parser,prompt2,model,parser)

print(result.invoke({'topic':'Genai'}))