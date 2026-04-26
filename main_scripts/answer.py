from helpers.retriever import provide_retriever_result
from langchain_openai import ChatOpenAI
from langchain.messages import SystemMessage, HumanMessage, AIMessage

def answer_the_question(question, messages):
  results = provide_retriever_result(question)

  relevant_content = ""

  for res in results:
    relevant_content += res.page_content
    relevant_content += "\n\n"

  user_prompt = f""" 
    Provide the answer to the questions aksed by user based on the context provided:

    question: {question}
    context: {relevant_content}
  """

  messages.append(HumanMessage(user_prompt))

  llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0, max_completion_tokens=200)

  response = llm.invoke(messages)

  return response.content


def ask_questions():
  messages = []

  system_prompt = SystemMessage(content="You are a chatbot representing Insure LLM and capable of answering questions asked by users. Please provide relevant and precise answer. Be on point and if you don't know something asked by the user say so. Respond to the user telling 'I am not sure about the answer please contact administrator for the same.'. If any question is asked out of the context provided in the user message, do not try to answer. Treat it as unknown answer" \
  "While answering make sure not to add any extra things like based on context etc., Just be straight with the answer")

  messages.append(system_prompt)

  while True:
    question = input("Please provide your question: ")

    if question == 'end' or question == 'exit':
      break

    response = answer_the_question(question=question, messages=messages)
    messages.append(AIMessage(response))
    print("\n", "Answer: ", response, "\n\n")


ask_questions()
