from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(
    model="Qwen/Qwen2.5-72B-Instruct", 
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic']
)

joke_gen_chain = RunnableSequence(prompt1,model,parser)

prompt2 = PromptTemplate(
    template = 'Explain the following joke - {text}',
    input_variables=['text']
)
parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'explanation' : RunnableSequence(prompt2,model,parser)
})

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)
res = final_chain.invoke({'topic':'programmer'})
print(res)