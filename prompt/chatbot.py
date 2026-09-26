from langchain_core import chat_history
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    model="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation",
    max_new_tokens=1000
)

model = ChatHuggingFace(llm=llm)

chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print('AI: ',result.content)

print(chat_history)