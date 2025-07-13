from langchain_openai import OpenAI
from dotenv import load_dotenv#Helps in loading the variables from .env file

load_dotenv

#Create an object of openai

llm=OpenAI(model="GPT-3.5")
#Will return text as answer

output=llm.invoke("What is the parameter of deepseek")

print(output)#These models only return string message as output