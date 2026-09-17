from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model = "openai/gpt-oss-120b")

prompt = 'What is the capital of India'
response = llm.invoke(prompt)
print(response)