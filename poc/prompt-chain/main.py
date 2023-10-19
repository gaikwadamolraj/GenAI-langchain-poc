from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = OpenAI(temperature=0.9)

prompt = PromptTemplate(input_variables = ["food"],
                       template= "What are best indian foods for someone who likes to eat {food}")

chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run('veg'))