from langchain.llms import OpenAI
from langchain.chains import ConversationChain

llm = OpenAI(temperature=0.9)
text = "What is the best indian food for the person who like most non veg?"
conversaton = ConversationChain(llm=llm, verbose=True)

conversaton.predict(input="Hi there")
conversaton.predict(input="I am doing well. Just having a conversation with an AI.")
conversaton.predict(input="Whas was the first thing I said to you?")
