from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(
    model="Qwen/Qwen2.5-72B-Instruct", 
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template='write a joke on {topic}',
    input_variables=['topic']
)
parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)
print(chain.invoke({'topic':'cricket'}))
