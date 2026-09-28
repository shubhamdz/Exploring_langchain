from abc import ABC, abstractmethod
import random


# 1. Base Runnable Class
class Runnable(ABC):

    @abstractmethod
    def invoke(self, input_data):
        pass


# 2. LLM Class
class NakliLLM(Runnable):

    def __init__(self):
        print("LLM created")

    def invoke(self, prompt):
        response_list = [
            "Delhi is the capital of India",
            "IPL is a cricket league",
            "AI stands for Artificial Intelligence"
        ]

        return {"response": random.choice(response_list)}


# 3. Prompt Template Class
class NakliPromptTemplate(Runnable):

    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def invoke(self, input_dict):
        return self.template.format(**input_dict)

    def format(self, input_dict):
        return self.template.format(**input_dict)


# 4. Output Parser Class
class NakliStrOutputParser(Runnable):

    def invoke(self, input_data):
        return input_data["response"]


# 5. Runnable Connector Class
class RunnableConnector(Runnable):

    def __init__(self, runnable_list):
        self.runnable_list = runnable_list

    def invoke(self, input_data):

        for runnable in self.runnable_list:
            input_data = runnable.invoke(input_data)

        return input_data


# 6. Create the LLM and Parser
llm = NakliLLM()
parser = NakliStrOutputParser()
template = NakliPromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['length', 'topic']
)

chain = RunnableConnector([template, llm, parser])

res = chain.invoke({'length':'long', 'topic':'india'})
print(res)