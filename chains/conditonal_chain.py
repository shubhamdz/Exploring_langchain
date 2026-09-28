from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableBranch,RunnableLambda
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()

llm = HuggingFaceEndpoint(
    model="Qwen/Qwen2.5-72B-Instruct", 
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
parser1 = StrOutputParser()

class feedback(BaseModel):
    sentiment: Literal['positive','negative'] = Field(description="Give the sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback into negative and postive \n {feedback} \n {format_instructions}",
    input_variables=['feedback'],
    partial_variables={'format_instructions':parser2.get_format_instructions()}
)

classifier_chain = prompt1|model|parser2

prompt2 = PromptTemplate(
    template=(
        "Write ONE short, friendly, and professional response "
        "to the following positive customer feedback. "
        "Do not provide multiple options, headings, or explanations.\n"
        "Feedback: {feedback}"
    ),
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template=(
        "Write ONE short, professional, and empathetic response "
        "to the following negative customer feedback. "
        "Do not provide multiple options, headings, or explanations.\n"
        "Feedback: {feedback}"
    ),
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x['sentiment'] == 'positive', prompt2 | model | parser1),
    (lambda x:x['sentiment'] == 'negative', prompt3 | model | parser1),
    RunnableLambda(lambda x: "could not find sentiment")
)

def prepare_branch_input(inputs):
    original_feedback = inputs['feedback']
    sentiment_result = classifier_chain.invoke({
        'feedback': original_feedback
    })

    return {
        'feedback': original_feedback,
        'sentiment': sentiment_result.sentiment
    }


chain = RunnableLambda(prepare_branch_input) | branch_chain


print(chain.invoke({
    'feedback': 'This is a terrible phone'
}))