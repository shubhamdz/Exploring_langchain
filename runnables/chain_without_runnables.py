import random


class NakliLLM:

    def __init__(self):
        print("LLM created")

    def predict(self, prompt):
        response_list = [
            "Delhi is the capital of India",
            "IPL is a cricket league",
            "AI stands for Artificial Intelligence"
        ]

        return {"response": random.choice(response_list)}


class NakliPromptTemplate:

    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict):
        return self.template.format(**input_dict)


class NakliLLMChain:

    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt

    def run(self, input_dict):
        final_prompt = self.prompt.format(input_dict)
        result = self.llm.predict(final_prompt)

        return result["response"]


# 1. Create the prompt template
template = NakliPromptTemplate(
    template="Write a {length} poem about {topic}",
    input_variables=["length", "topic"]
)

# 2. Format the prompt
prompt = template.format({
    "length": "short",
    "topic": "india"
})

print("Formatted Prompt:", prompt)

# 3. Create the LLM
llm = NakliLLM()

# 4. Call the LLM directly
print("Direct LLM Response:", llm.predict(prompt))

# 5. Create the chain
chain = NakliLLMChain(llm, template)

# 6. Execute the chain
response = chain.run({
    "length": "short",
    "topic": "india"
})

print("Chain Response:", response)