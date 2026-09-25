from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    model="Qwen/Qwen2.5-72B-Instruct", 
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("what is the capital of India")
print(result.content)
