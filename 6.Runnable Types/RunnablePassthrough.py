from langchain_google_genai  import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough

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

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

print(final_chain.invoke({'topic':'cricket'}))