from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

#Configuration of llm's
llm=HuggingFaceEndpoint(repo_id="moonshotai/Kimi-K2-Instruct",
                      task="text-generation")

model=ChatHuggingFace(llm=llm)

result=model.invoke("List of greatest football players of all time")
print(result.content)

