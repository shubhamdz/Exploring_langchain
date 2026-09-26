from platform import system
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'you are a helpful {domain} expert'),
    ('human','Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'Machine Learning', 'topic':'Neural Network'})

print(prompt)