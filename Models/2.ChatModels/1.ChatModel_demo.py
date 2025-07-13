from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model="gpt-4",temperature=0.1,max_completion_tokens=50)
#Temperature is parameter that controls randomness of output.Affects how creative responsees are
#0-0.3:Math questions
# 0.5-0.7:General QA
#0.7-1.2:Creative story,Telling jokes
#1.5+:Highly creative tasks(brainstorming)

#max_completion_tokens:Max no of tokens u need for output


result=model.invoke("Capital of India")
print(result)#Prints additional information as well
print(result.content)#Prints only the main answer