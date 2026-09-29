from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnableLambda,RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(
    model="Qwen/Qwen2.5-72B-Instruct", 
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

prompt = PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic']
)

joke_gen_chain = RunnableSequence(prompt,model,parser)

def word_counter(text):
    return len(text.split())

parallel_chain =  RunnableParallel({
    'joke': RunnablePassthrough(),
    'number of words': RunnableLambda(word_counter) 

})

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)
res = final_chain.invoke({'topic':'programmer'})
print(res)
