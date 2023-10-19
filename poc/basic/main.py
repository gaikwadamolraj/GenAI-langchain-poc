from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)
text = "What is the best indian food for the person who like most non veg?"

print(llm(text))