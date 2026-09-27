from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    model="Qwen/Qwen2.5-72B-Instruct", 
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)


parser = JsonOutputParser()

template = PromptTemplate(
    template= 'Give me the name, age and city of a fictional person \n {format_instruction}',
    input_variables = [],
    partial_variables= {'format_instruction' : parser.get_format_instructions()}  
)

prompt = template.invoke({})

result = model.invoke(prompt)

final_result = parser.parse(result.content)

#OR 

# chain = template | model | parser
# final_result = chain.invoke({})



print(final_result)
print(type(final_result))