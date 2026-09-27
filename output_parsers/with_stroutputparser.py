from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    model="Qwen/Qwen2.5-72B-Instruct", 
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

#1st prompt -> detailed report

template1 = PromptTemplate(
    template='write detailed report on {topic}',
    input_variables=['topic']
)

#2nd prompt -> summary

template2 = PromptTemplate(
    template='write a 5 line summary on the following text.\n{text}',
    input_variables=['text']
)

praser = StrOutputParser()

chain = template1 | model | praser | template2 | model | praser

result = chain.invoke({'topic' : 'black hole'})

print(result)
