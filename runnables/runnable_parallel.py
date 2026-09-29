from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel
from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(
    model="Qwen/Qwen2.5-72B-Instruct", 
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)
 
prompt2 = PromptTemplate(
    template='Generate a linkedin post about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()
    
parallel_chain = RunnableParallel({
    'tweet': prompt1|model|parser,
    'linkedin': prompt2|model|parser
})

res = parallel_chain.invoke({'topic':'AI'})
print(res)