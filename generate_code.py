from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

def get_api_code(user_input):
    question_template = """
    You are an expert Python API developer. The user needs an API with the following requirements: {user_input}. 
    Generate the complete FastAPI code, including authentication and pagination. Return only code and nothing else.
    """

    template = """Question: {question}

    Answer: Let's think step by step."""

    prompt = ChatPromptTemplate.from_template(template)
    model = OllamaLLM(model="llama3")
    chain = prompt | model
    return chain.invoke({"question": question_template})